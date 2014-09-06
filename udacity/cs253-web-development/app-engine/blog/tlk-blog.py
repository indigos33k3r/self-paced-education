from datetime import datetime
from google.appengine.api import memcache
from google.appengine.ext import db
from passlib.hash import sha512_crypt
import collections, jinja2, json, logging, os, re, webapp2

secret = 'ahDjEadPFdR4Pik'
blog_key = db.Key.from_path('blog', 'blog')
time = collections.defaultdict(datetime.now)

def blog_posts(update=False):
    key = 'blog'
    posts = memcache.get(key)
    if posts is None or update:
        posts = list(db.GqlQuery('SELECT * '
                                 'FROM Post '
                                 'WHERE ANCESTOR IS :1 '
                                 'ORDER BY created DESC',
                                 blog_key))
        time[key] = datetime.now()
        memcache.set(key, posts)
    return posts

def encrypt_secure_value(value):
    return sha512_crypt.encrypt(value + secret)

def verify_secure_value(value, hash):
    return sha512_crypt.verify(value + secret, hash)

def is_empty(s):
    return True if s.strip() == '' else False

def verify_username(username):
    return re.match('^[A-Za-z0-9_-]{3,20}$', username)

def verify_password(password):
    return re.match('^.{3,20}$', password)

def verify_verify(password, verify):
    return verify_password(password) and password == verify

def verify_email(email):
    return is_empty(email) or re.match('^[\S]+@[\S]+\.[\S]+$', email)

class Post(db.Model):
    subject = db.StringProperty(required=True)
    content = db.TextProperty(required=True)
    created = db.DateTimeProperty(auto_now_add=True)
    last_modified = db.DateTimeProperty(auto_now_add=True)

    @classmethod
    def by_id(cls, id):
        key = id
        try:
            key_int = int(key)
        except KeyError:
            return None

        post = memcache.get(key)
        if post is None:
            post = Post.get_by_id(key_int, parent=blog_key)
            time[key] = datetime.now()
            memcache.set(key, post)
        return post

    def json(self):
        date_format = '%a %b %d %H:%M:%S %Y'
        return {
            'subject': self.subject,
            'content': self.content,
            'created': self.created.strftime(date_format),
            'last_modified': self.last_modified.strftime(date_format)
        }

class User(db.Model):
    username = db.StringProperty(required=True)
    password_hash = db.StringProperty(required=True)
    email = db.EmailProperty()

    @classmethod
    def by_username(cls, username):
        return db.GqlQuery("SELECT * FROM User WHERE username = :1",
                           username).get()

    @classmethod
    def register(cls, username, password, email):
        return User(username=username,
                    password_hash=sha512_crypt.encrypt(password),
                    email=(None if is_empty(email) else email))

    @classmethod
    def login(cls, username, password):
        user = cls.by_username(username)
        if user is not None and user.verify_password(password):
            return user

    def verify_password(self, password):
        try:
            if sha512_crypt.verify(password, self.password_hash):
                return True
            else:
                return False
        except (TypeError, ValueError):
            return False

class Handler(webapp2.RequestHandler):
    def write(self, *a, **kw):
        self.response.out.write(*a, **kw)

    def render_str(self, template, **params):
        t = jinja_env.get_template(template)
        return t.render(params)

    def render(self, template, **kw):
        self.write(self.render_str(template, **kw))

    def set_cookie(self, name, value):
        self.response.headers.add_header(
            'Set-Cookie',
            '{}={}; Path=/'.format(name, value)
        )

    def set_secure_cookie(self, name, value):
        self.response.headers.add_header(
            'Set-Cookie',
            '{}={}; Path=/'.format(name, encrypt_secure_value(value))
        )

    def check_secure_cookie(self, cookie_name, hash_name):
        value = self.request.cookies.get(cookie_name)
        hash = self.request.cookies.get(hash_name)
        if cookie_name == 'username' and not User.by_username(value):
            return False

        try:
            return True if sha512_crypt.verify(value + secret, hash) else False
        except (TypeError, ValueError):
            return False

    def delete_cookie(self, name):
        self.response.headers.add_header(
            'Set-Cookie',
            '{}=; expires=Thu, 01-Jan-70 00:00:01 GMT'.format(name)
        )

    def login(self, username):
        self.set_cookie('username', username)
        self.set_secure_cookie('username_hash', username)

    def logout(self):
        self.delete_cookie('username')
        self.delete_cookie('username_hash')

class MainPage(Handler):
    def get(self):
        posts = blog_posts()
        self.render('front.html',
                    posts=posts,
                    seconds=(datetime.now() - time['blog']).seconds)

class MainJSON(Handler):
    def get(self):
        posts = blog_posts()
        self.response.headers['Content-Type'] = 'application/json'
        self.write(json.dumps([post.json() for post in posts]))

class SignUpPage(Handler):
    def render_page(self, username='', username_error='', password_error='',
                    verify_error='', email='', email_error=''):
        self.render('signup.html', username=username,
                    username_error=username_error,
                    password_error=password_error, verify_error=verify_error,
                    email=email, email_error=email_error)

    def get(self):
        self.render_page()

    def post(self):
        username = self.request.get('username').strip()
        password = self.request.get('password')
        verify = self.request.get('verify')
        email = self.request.get('email').strip()

        if not (verify_username(username) and
                User.by_username(username) is None and
                verify_password(password) and
                verify_verify(password, verify) and
                verify_email(email)):
            if not verify_username(username):
                username_error = 'Must be 3-20 characters (A-Za-z_-) long.'
            elif User.by_username(username) is not None:
                username_error = 'Username already taken.'
            else:
                username_error = ''

            if not verify_password(password):
                password_error = 'Must be 3-20 characters long.'
            else:
                password_error = ''

            if not verify_verify(password, verify):
                verify_error = 'Must match password.'
            else:
                verify_error = ''

            if not verify_email(email):
                email_error = 'Must be valid-ish.'
            else:
                email_error = ''

            self.render_page(username=username,
                             username_error=username_error,
                             password_error=password_error,
                             verify_error=verify_error,
                             email=email,
                             email_error=email_error)
        else:
            u = User.register(username, password, email)
            u.put()
            self.login(username)
            self.redirect('/welcome')

class LoginPage(Handler):
    def render_page(self, username='', error=''):
        self.render('login.html', username=username, error=error)

    def get(self):
        self.render_page()

    def post(self):
        username = self.request.get('username')
        password = self.request.get('password')
        if User.login(username, password) is not None:
            self.login(username)
            self.redirect('/welcome')
        else:
            self.render_page(username, 'Invalid login provided.')

class LogoutPage(Handler):
    def get(self):
        self.logout()
        self.redirect('/signup')

class WelcomePage(Handler):
    def get(self):
        if self.check_secure_cookie('username', 'username_hash'):
            self.render('welcome.html',
                        username=self.request.cookies.get('username'))
        else:
            self.redirect('/signup')

class NewPostPage(Handler):
    def render_page(self, subject='', content='', error=''):
        self.render('new.html', subject=subject, content=content, error=error)

    def get(self):
        self.render_page()

    def post(self):
        subject = self.request.get('subject')
        content = self.request.get('content')
        if subject and content:
            new_post = Post(subject=subject,
                            content=content.replace('\n', '<br />'),
                            parent=blog_key)
            new_post.put()
            blog_posts(update=True)
            self.redirect('/post/{}'.format(new_post.key().id()))
        else:
            error = 'Both a subject and some content are required!'
            self.render_page(subject, content, error)

class PostPage(Handler):
    def get(self, post_id):
        post = Post.by_id(post_id)
        if post:
            self.render('post.html',
                        post=post,
                        seconds=(datetime.now() - time['post_id']).seconds)
        else:
            self.abort(404)

class PostJSON(Handler):
    def get(self, post_id):
        post = Post.by_id(post_id)
        if post:
            self.response.headers['Content-Type'] = 'application/json'
            self.write(json.dumps(post.json()))
        else:
            self.abort(404)

class FlushPage(Handler):
    def get(self):
        memcache.flush_all()
        self.redirect('/')

template_dir = os.path.join(os.path.dirname(__file__), 'templates')
jinja_env = jinja2.Environment(loader=jinja2.FileSystemLoader(template_dir),
                               autoescape=True)

application = webapp2.WSGIApplication([
    ('/', MainPage),
    ('/.json/?', MainJSON),
    ('/signup/?', SignUpPage),
    ('/login/?', LoginPage),
    ('/logout/?', LogoutPage),
    ('/welcome/?', WelcomePage),
    ('/newpost/?', NewPostPage),
    ('/post/([0-9]+)/?', PostPage),
    ('/post/([0-9]+)\.json/?', PostJSON),
    ('/flush/?', FlushPage),
], debug=True)
