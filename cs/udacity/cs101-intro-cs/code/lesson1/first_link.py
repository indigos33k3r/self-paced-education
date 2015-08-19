# Write Python code that assigns to the variable url a string that is the value 
# of the first URL that appears in a link tag in the string page.
# Your code should print http://udacity.com. Make sure that if page 
# were changed to page = '<a href="http://udacity.com">Hello world</a>'
# that your code still prints the same thing.

#note: things like str.replace() and the way I handled extra cases are not necessary for this lesson

# page = contents of a web page
page = """
        <div id="top_bin"><div id="top_content" class="width960">
          <a class = "email_link" href="http://mail.google.com" style="color: red;">Gmail</a>
            <div class="udacity float-left">
                <a href="http://udacity.com">Udacity</a>
            </div>
        </div>
"""

repl = ['= ', ' =', ' = ']

for i in range(0, len(repl)):
  page = page.replace(repl[i], "=")

first_link = page.find("<a")
first_url_start = page.find("href=", first_link) + len("href=") + 1

if page[page.find("href=", first_link) + len("href=")] == '"':
  first_url = page[first_url_start:page.find('"', first_url_start)]
else:
  first_url = page[first_url_start:page.find("'", first_url_start)]

print first_url