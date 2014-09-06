import webapp2, cgi

form = """

<html lang="en">
  <head>
    <title>Ty's ROT 13 for Unit 2, Udacity CS253</title>
    <meta name="description" content="Udacity CS253: ROT13">
    <link href='http://fonts.googleapis.com/css?family=Lato:100,300,400,700,100italic,300italic,400italic,700italic' rel='stylesheet' type='text/css'>
    <style type="text/css">
      body {
        font-family: 'Lato', sans-serif;
      }

      h1 {
        font-weight: 300;
        font-size: 2.25em;
      }

      h2 {
        font-weight: 200;
        font-size: 1.5em;
      }

      div {
        max-width: 400px;
      }

      p {
        font-weight: 300;
        font-size: 1em;
      }
    </style>
  </head>
  <body>
    <h1>Udacity: CS253, Unit 2</h1>
    <h2>ROT 13</h2>
    <div>
      <p>
        ROT13 is a simple cypher in which each letter in the text you
        enter gets shifted by 13 letters.
        This means that applying ROT13 to some text will
        cause it to shift after one attempt,
        and then revert to the original after a second one! Pretty cool.
      </p>
    </div>
    <form method="post">
      <textarea name="text" rows="10" cols="50" name="text" placeholder="Enter text here!">%(user_input)s</textarea><br><br>
      <input type="submit">
    </form>
  </body>
</html>

"""

# Classes

class FormPage(webapp2.RequestHandler):
  def display_form(self, user_input=''):
    self.response.out.write(form % { 'user_input': rot13(user_input) })

  def get(self):
    self.display_form()

  def post(self):
    text = self.request.get('text')
    self.display_form(text)

# Functions

def rot13(s):
  return cgi.escape(s.encode('rot13'))

# Handlers

application = webapp2.WSGIApplication(
  [
    ('/', FormPage)
  ], debug=True)
