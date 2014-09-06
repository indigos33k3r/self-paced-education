#imports

import os, webapp2, jinja2, re
from google.appengine.ext import db
from google.appengine.api import memcache

#variables

template_dir = os.path.join(os.path.dirname(__file__), 'templates')
jinja_env = jinja2.Environment(loader = jinja2.FileSystemLoader(template_dir), autoescape=True)
art_key = db.Key.from_path('ASCIIChan', 'arts')

#art entity

class Art(db.Model):
  title = db.StringProperty(required = True)
  art = db.TextProperty(required = True)
  created = db.DateTimeProperty(auto_now_add = True)

#handler base class

class Handler(webapp2.RequestHandler):
  def write(self, *a, **kw):
    self.response.out.write(*a, **kw)

  def render_str(self,template, **params):
    t = jinja_env.get_template(template)
    return t.render(params)

  def render(self,template, **kw):
    self.write(self.render_str(template, **kw))

#main page handler

class MainPage(Handler):
  def render_front(self, title = "" , art = "", error = ""):
    arts = top_arts()
    self.render("front.html", title = title, art = art, error = error, arts = arts)

  def get(self):
    self.render_front()

  def post(self):
    title = self.request.get("title")
    art = self.request.get("art")

    if title and art:
      if len(title) > 500000 or len(art) > 500000:
        error = "Your input is too large to store!"
        self.render_front(title, art, error)
      else:
        a = Art(parent = art_key, title = title, art = art)
        a.put()
        top_arts(True)
        self.redirect("/")
    else:
      error = "we need both a title and some artwork!"
      self.render_front(title, art, error)

#flush cache

class FlushCache(Handler):
  def get(self):
    memcache.flush_all()
    self.redirect('/')

#functions

def top_arts(update = False):
  key = 'top'
  arts = memcache.get(key)

  if arts is None or update:
    arts = db.GqlQuery("SELECT * FROM Art WHERE ANCESTOR IS :1 ORDER BY created DESC LIMIT 1000", art_key)
    arts = list(arts)
    memcache.set(key, arts)

  return arts

# define application

application = webapp2.WSGIApplication([
  ('/', MainPage),
  ('/flush', FlushCache)
], debug = True)
