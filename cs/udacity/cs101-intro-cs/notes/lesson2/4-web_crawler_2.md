#Intro to Computer Science

**Udacity: CS 101**

---

###The Web Crawler, Continued

We now know enough to get **all** of the links from a webpage, not just the first one. Remember how we turned our code to get the first link on a given page into a procedure? The next step is to keep trimming the input (called `page` in our case) until we are out of links to grab. This is where loops can come in handy!

But first, a bit on *multiple assignment*. Since procedures can return multiple values, we need to be able to use all of them! It's pretty simple in Python:

	def two_values():
		return 1, 2
		
	# multiple assignment
	a, b = two_values()
	
	print a
	
	>>> 1
	
	print b
	
	>>> 2

Easy, right? Here's a cool use of multiple assignment:

	a = 1
	b = 2
	
	a, b = b, a
	
	# we just swapped the values of a and b!

Anyway, back to the web crawler. Here's what our `get_next_target` procedure looks like as of now:

	def get_next_target(page):
		copy = page
		repl = ['= ', ' =', ' = ']
		for i in range(0, len(repl)):
			copy = copy.replace(repl[i], "=")

		first_link_start = copy.find("<a")
		first_url_start = copy.find("href=", first_link_start) + len("href=") + 1

		if (copy[copy.find("href=", first_link_start) + len("href=")] == '"'):
			url = copy[first_url_start:copy.find('"', first_url_start)]
		else:
			url = copy[first_url_start:copy.find("'", first_url_start)]

		first_url_end = page.find(url) + len(url) + 1
		return url, first_url_end
			
There's one serious problem with this procedure. What happens if we have a page with no links? Right now, we'd get some garbage for `url` and an error for `first_url_end`. What we need is a way to tell our procedure to return `None` when there is no link to be found. Here's one way to go about it:

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
			
What the code now does is return `None` if the input string contains no link tags. This procedure is now ready to be put to use! Let's make another procedure, called `print_all_links`. It will work by passing in the initial seed page, and then using the second return value from `get_next_target`, called `first_url_end` to chop off the first url from `page`. It will use a `while` loop to continue chopping off the first link from page until there are no more links:

	def print_all_links(page):
		while (get_next_target(page) != None):
			url, next_start = get_next_target(page)
			print url
			page = page[next_start:]
			
Try these two methods out using this sample page:

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
	
You should get this output by calling `print_all_links`:

	http://mail.google.com
	http://udacity.com
	https://facebook.com
	
We can now get all of the links from any webpage!  We aren't done with our web crawler just yet, but it's getting there.