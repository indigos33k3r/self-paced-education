import os, webapp2, jinja2

cwd = os.path.dirname(__file__)
template_dir = os.path.join(cwd, 'templates')
jinja_env = jinja2.Environment(loader = jinja2.FileSystemLoader(template_dir), autoescape=True) # automatically HTML escapes for safety

class Handler(webapp2.RequestHandler):
  def write(self, *a, **kw):
    self.response.out.write(*a, **kw)

  def render_str(self, template, **params):
    t = jinja_env.get_template(template)
    return t.render(params)

  def render(self, template, **kw):
    self.write(self.render_str(template, **kw))


class MainPage(Handler):
  def get(self):
    items = self.request.get_all('food')
    self.render('shopping.html', items=items)

application = webapp2.WSGIApplication(
  [
    ('/', MainPage),
  ],
  debug=True)
