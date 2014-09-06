import webapp2

form = """

<form method="post">
	What is your birthday?
	<br><br>
	<input type="text" name="month" value="%(month)s" placeholder="Month">
	<input type="text" name="day" value="%(day)s" placeholder="Day">
	<input type="text" name="year" value="%(year)s" placeholder="Year">
	<br><br>
	<div style="color: red;">%(error)s</div><br>
	<input type="submit">
</form>

"""

class MainPage(webapp2.RequestHandler):
	def print_form(self, error='', month='', day='', year=''):
		self.response.out.write(form % {'error': error,
																		'month': escape(month),
																		'day': escape(day),
																		'year': escape(year)});
	def get(self):
		self.print_form()

	def post(self):
		month = self.request.get('month')
		day = self.request.get('day')
		year = self.request.get('year')

		if not (valid_month(month) and valid_day(day) and valid_year(year)):
			self.print_form("Invalid inputs!", month, day, year)
		else:
			self.redirect("/thanks")

class ThanksHandler(webapp2.RequestHandler):
	def get(self):
		self.response.out.write("Thanks for submitting")




months = [
	'Janurary',
	'February',
	'March',
	'April',
	'May',
	'June',
	'July',
	'August',
	'September',
	'October',
	'November',
	'December'
]

def valid_month(month):
	for x in months:
		if month.lower() == x.lower():
			return x
	return None


def valid_year(year):
	if year.isdigit():
		if (int(year) >= 1900 and int(year) <= 2014):
			return int(year)
	return None


def valid_day(day):
	if day.isdigit():
		if (int(day) >= 1 and int(day) <= 31):
			return int(day)
	return None

def escape(s):
	html_escape = {
		"&": "&amp;",
		'"': "&quot;",
		"'": "&apos;",
		">": "&gt;",
		"<": "&lt;",
		}
	return "".join(html_escape.get(c,c) for c in s)

application = webapp2.WSGIApplication(
	[
		('/', MainPage), ('/thanks', ThanksHandler)
	],
	debug=True)
