from google.appengine.ext import db
from passlib.hash import sha512_crypt
import bleach
import jinja2
import markdown
import os
import re
import webapp2

PAGE_RE = r'(/(?:[a-zA-Z0-9_-]+/?)*)'
SECRET = 'ahDjEadPFdR4Pik'
TAG_WHITELIST = [u'a', u'abbr', u'acronym', u'audio', u'b', u'blockquote',
                 u'br', u'code', u'del', u'em', u'h1', u'h2', u'h3', u'h4',
                 u'h5', u'h6', u'hr', u'i', u'img', u'ins', u'li', u'mark',
                 u'ol', u'p', u'pre', u'q', u'source', u'strong', u'sub',
                 u'sup', u'ul', u'video', u'wbr']
USER_KEY = db.Key.from_path('user', 'user')
WIKI_KEY = db.Key.from_path('wiki', 'wiki')


def encrypt_secure_value(value):
    return sha512_crypt.encrypt(value + SECRET)


def verify_secure_value(value, hash):
    return sha512_crypt.verify(value + SECRET, hash)


def is_empty(s):
    return True if s.strip() == '' else False


def verify_username(username):
    return re.match(r'^[A-Za-z0-9_-]{3,20}$', username)


def verify_password(password):
    return re.match(r'^.{3,20}$', password)


def verify_verify(password, verify):
    return verify_password(password) and password == verify


def verify_email(email):
    return is_empty(email) or re.match(r'^[\S]+@[\S]+\.[\S]+$', email)


class Topic:
    def __init__(self, path):
        """Represents a wiki topic to deal with forward slash characters."""
        self.path = path
        self.edit_name = self.display_name(path, 'edit')
        self.wiki_name = self.display_name(path, 'wiki')

    def display_name(self, path, display_type='wiki'):
        """Returns a name for context-dependent display (wiki/edit pages)."""
        slash = '/'
        if path == slash:
            if display_type == 'wiki':
                return ''
            else:
                return path
        elif path.startswith(slash):
            return path.lstrip(slash)
        else:
            return path


class Wiki(db.Model):
    topic = db.StringProperty(required=True)
    content = db.TextProperty(required=True)
    created = db.DateTimeProperty(auto_now_add=True)

    @classmethod
    def ordered_by_topic(cls, topic):
        """Returns a Query object with wikis for the topic in time order.

        Time order is in descending order by create date."""
        wikis = Wiki.all().ancestor(WIKI_KEY)
        return wikis.filter("topic =", topic.path).order("-created")

    @classmethod
    def latest_by_topic(cls, topic):
        """Returns the latest wiki for the given topic.

        If it doesn't exist, returns None."""
        return cls.ordered_by_topic(topic).get()

    @classmethod
    def by_id_or_latest_by_topic(cls, topic, id):
        """Returns the wiki for the given topic and ID if possible.

        Otherwise, returns the latest wiki for the given topic. If neither
        exist, returns None."""
        key = id
        try:
            key_int = int(key)
            wiki = Wiki.get_by_id(key_int, parent=WIKI_KEY)
            if wiki is not None and wiki.topic == topic.path:
                return wiki
            else:
                return cls.latest_by_topic(topic)
        except (KeyError, TypeError, ValueError):
            return cls.latest_by_topic(topic)


class User(db.Model):
    username = db.StringProperty(required=True)
    password_hash = db.StringProperty(required=True)
    email = db.EmailProperty()

    @classmethod
    def by_username(cls, username):
        user = User.all().ancestor(USER_KEY).filter("username =", username)
        return user.get()

    @classmethod
    def register(cls, username, password, email):
        return User(username=username,
                    password_hash=sha512_crypt.encrypt(password),
                    email=(None if is_empty(email) else email),
                    parent=USER_KEY)

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
            return True if sha512_crypt.verify(value + SECRET, hash) else False
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

    def is_logged_in(self):
        if self.check_secure_cookie('username', 'username_hash'):
            return True
        else:
            return False

    def logged_in_user(self):
        if self.is_logged_in():
            return self.request.cookies.get('username')
        else:
            return ''

    def logout(self):
        self.delete_cookie('username')
        self.delete_cookie('username_hash')


class SignUpPage(Handler):
    def render_page(self, username='', username_error='', password_error='',
                    verify_error='', email='', email_error='', redirect=''):
        self.render('signup.html',
                    username=username, username_error=username_error,
                    password_error=password_error, verify_error=verify_error,
                    email=email, email_error=email_error,
                    redirect=redirect)

    def get(self):
        redirect = self.request.get('redirect')
        if self.is_logged_in():
            if redirect:
                self.redirect(redirect)
            else:
                self.redirect('/')
        else:
            self.render_page(redirect=redirect)

    def post(self):
        username = self.request.get('username').strip()
        password = self.request.get('password')
        verify = self.request.get('verify')
        email = self.request.get('email').strip()
        redirect = self.request.get('redirect')

        params = {'username': username, 'email': email, 'redirect': redirect}
        errors_exist = False
        if not verify_username(username):
            params['username_error'] = 'Must be 3-20 characters (A-Za-z_-).'
            errors_exist = True
        elif User.by_username(username) is not None:
            params['username_error'] = 'Username already taken.'
            errors_exist = True
        if not verify_password(password):
            params['password_error'] = 'Must be 3-20 characters.'
            errors_exist = True
        if not verify_verify(password, verify):
            params['verify_error'] = 'Must match password.'
            errors_exist = True
        if not verify_email(email):
            params['email_error'] = 'Must be valid-ish.'
            errors_exist = True

        if errors_exist:
            self.render_page(**params)
        else:
            user = User.register(username, password, email)
            user.put()
            self.login(username)
            if redirect:
                self.redirect(redirect)
            else:
                self.redirect('/')


class LoginPage(Handler):
    def render_page(self, username='', redirect='', error=''):
        self.render('login.html', username=username, redirect=redirect,
                    error=error)

    def get(self):
        redirect = self.request.get('redirect')
        if self.is_logged_in():
            if redirect:
                self.redirect(redirect)
            else:
                self.redirect('/')
        else:
            self.render_page(redirect=redirect)

    def post(self):
        username = self.request.get('username')
        password = self.request.get('password')
        redirect = self.request.get('redirect')
        if User.login(username, password) is not None:
            self.login(username)
            if redirect:
                self.redirect(redirect)
            else:
                self.redirect('/')
        else:
            self.render_page(username=username,
                             redirect=redirect,
                             error='Invalid login provided.')


class LogoutPage(Handler):
    def get(self):
        self.logout()
        redirect = self.request.get('redirect')
        if redirect:
            self.redirect(redirect)
        else:
            self.redirect('/')


class WikiPage(Handler):
    def render_page(self, topic='', id='', content='', username=''):
        self.render('wiki.html',
                    topic=topic, id=id, content=content, username=username)

    def get(self, path):
        topic = Topic(path)
        id = self.request.get('id')
        wiki = Wiki.by_id_or_latest_by_topic(topic, id)
        if wiki is not None:
            content = bleach.clean(markdown.markdown(wiki.content),
                                   tags=TAG_WHITELIST)
            self.render_page(topic=topic,
                             id=id,
                             content=content,
                             username=self.logged_in_user())
        else:
            self.redirect('/_edit{}'.format(path))


class EditPage(Handler):
    def render_page(self, topic='', id='', content='', view_link=False,
                    username='', error=''):
        self.render('edit.html',
                    topic=topic, id=id, content=content, view_link=view_link,
                    username=username, error=error)

    def get(self, path):
        topic = Topic(path)
        if topic.edit_name in ['login', 'logout', 'signup']:
            self.redirect('/')
        elif not self.is_logged_in():
            self.redirect('/login?redirect=/_edit{}'.format(path))
        else:
            id = self.request.get('id')
            wiki = Wiki.by_id_or_latest_by_topic(topic, id)
            self.render_page(topic=topic,
                             id=id,
                             content=wiki.content if wiki else '',
                             view_link=True if wiki else False,
                             username=self.logged_in_user())

    def post(self, path):
        if self.is_logged_in():
            topic = Topic(path)
            id = self.request.get('id')
            old_wiki = Wiki.latest_by_topic(topic)
            new_wiki_content = self.request.get('content')
            username = self.logged_in_user()
            if not is_empty(new_wiki_content):
                if old_wiki is None or new_wiki_content != old_wiki.content:
                    wiki = Wiki(topic=topic.path,
                                content=new_wiki_content,
                                parent=WIKI_KEY)
                    wiki.put()
                self.redirect(path)
            else:
                self.render_page(topic=topic,
                                 id=id,
                                 view_link=True if old_wiki else False,
                                 username=username,
                                 error='Some content is required!')
        else:
            self.redirect(path)


class HistoryPage(Handler):
    def render_page(self, topic='', id='', wikis=None, username=''):
        if wikis is None:
            wikis = []

        self.render('history.html',
                    topic=topic, id=id, wikis=wikis, username=username)

    def get(self, path):
        topic = Topic(path)
        id = self.request.get('id')
        wikis = Wiki.ordered_by_topic(topic)
        wikis_list = []
        for wiki in wikis:
            content = bleach.clean(markdown.markdown(wiki.content),
                                   tags=TAG_WHITELIST)
            wikis_list.append({'id': wiki.key().id(),
                               'created': wiki.created,
                               'content': content})

        if wikis_list:
            self.render_page(topic=topic,
                             id=id,
                             wikis=wikis_list,
                             username=self.logged_in_user())
        else:
            self.redirect('/_edit{}'.format(path))


template_dir = os.path.join(os.path.dirname(__file__), 'templates')
jinja_env = jinja2.Environment(loader=jinja2.FileSystemLoader(template_dir),
                               autoescape=True)

application = webapp2.WSGIApplication([
    ('/signup/?', SignUpPage),
    ('/login/?', LoginPage),
    ('/logout/?', LogoutPage),
    ('/_edit{}'.format(PAGE_RE), EditPage),
    ('/_history{}'.format(PAGE_RE), HistoryPage),
    (PAGE_RE, WikiPage),
], debug=True)
