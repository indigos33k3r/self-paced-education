# gets the first link on any webpage
def get_next_target(page):
  copy = page
  repl = ['= ', ' =', ' = ']
  for i in range(0, len(repl)):
    copy = copy.replace(repl[i], "=")

  first_link_start = copy.find("<a")
	
  if (first_link_start == -1):
    return None
  else:
    first_url_start = copy.find("href=", first_link_start) + len("href=") + 1

    if (copy[copy.find("href=", first_link_start) + len("href=")] == '"'):
      url = copy[first_url_start:copy.find('"', first_url_start)]
    else:
      url = copy[first_url_start:copy.find("'", first_url_start)]

    first_url_end = page.find(url) + len(url) + 1
    return url, first_url_end

# prints out all of the links on a webpage
# it works by trimming off the first link from the page until there are none left
def get_all_links(page):
  links = []
  while (get_next_target(page) != None):
    url, marker = get_next_target(page)
    links.append(url)
    page = page[marker:]
  return links

# page = contents of a web page
page = """
        <div id="top_bin"><div id="top_content" class="width960">
          <a class = "email_link" href="http://mail.google.com" style="color: red;">Gmail</a>
            <div class="udacity float-left">
                <a href="http://udacity.com">Udacity</a>
            </div>
			<section class="grid12" id="my_section">
				<a class ="facebook" id="fb" href = "https://facebook.com">
					<img src="http://my-site.com/img/fb.png">
				</a>
			</section>
        </div>
"""

# let's store and then print out all of the links!
links = get_all_links(page)
print links