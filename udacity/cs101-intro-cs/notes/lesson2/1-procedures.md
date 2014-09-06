#Intro to Computer Science

**Udacity: CS 101**

---

###Lesson 2: Introduction

**What we've covered so far**

* An introduction to what programming is all about: using computers to solve problems
* A history and introduction to Python
* The importance of grammar and Backus-Naur Form
* Doing arithmetic
* Dealing with strings: printing them, indexing, manipulating, etc
* Solving small problems, like finding the first link on a webpage
* Reading documentation and using online resources

**What we will cover in this lesson**

* Procedures
* If-else statements
* Loops
* Making our web crawler find all of the links on a page

###Procedures

Procedures are a way of packing code so it can be reused easily. Recall our code for finding the first link on a webpage:

	repl = ['= ', ' =', ' = ']

	for i in range(0, len(repl)):
		page = page.replace(repl[i], "=")

	first_link = page.find("<a")
	first_url_start = page.find("href=", first_link) + len("href=") + 1

	if page[page.find("href=", first_link) + len("href=")] == '"':
		first_url = page[first_url_start:page.find('"', first_url_start)]
	else:
		first_url = page[first_url_start:page.find("'", first_url_start)]
		
What if we wanted to find all of the links on a webpage? Well, to get the next one, we could add this line to the code:

	page = page[first_url_start + len(first_url):]
	
This would let us find the second link, by getting rid of everything up to the end of the first link. We'd have to rewrite all that code again though. This would not scale at all! Imagine re-writing our code 1000 times if we wanted to find 1000 links on a page. *Yikes...*

What we need to do involves something called *procedural abstraction*. Let's take all that code we use to get a link from the page, knowing that the only thing that changes is the input (the value of `page`), and make it a *procedure* that can handle changing input. A procedure is defined like this in Python:

	def foo():
		# code goes here. indentation matters!
		print "foo"

	# this is not part of the procedure anymore
	
	foo()
	
	>>> "foo"
		
A procedure takes input, does something with it, and generates an output based on that input. We've seen some procedures before: `+`, `str.find()`, and `len()` are all built-in procedures (not quite, but they basically are).

The name of a procedure can be anything that is also a legal variable name. Note the parentheses, colon, and indentation! We can have an unlimited number of inputs, separated by commas like this: `def foo(bar, baz):` (we can also have no inputs, as above).

The inputs, also called *parameters*, should have useful names, like `page` in our case.

Let's turn our link-extracting code into a procedure! As we know, the input should be the webpage. Let's call it `page`, as we have been already. We will modify the code just a bit to make the output easier to generate:

	def get_next_target(page):
		copy = page
		repl = ['= ', ' =', ' = ']
		for i in range(0, len(repl)):
			copy = copy.replace(repl[i], "=")

		first_link_start = copy.find("<a")
		first_url_start = copy.find("href=", first_link_start) + len("href=") + 1
	
		if copy[copy.find("href=", first_link_start) + len("href=")] == '"':
			url = copy[first_url_start:copy.find('"', first_url_start)]
		else:
			url = copy[first_url_start:copy.find("'", first_url_start)]

		first_url_end = page.find(url) + len(url) + 1
		return url, first_url_end

* Note: variables defined within a procedure **cannot** be accessed from outside of the procedure. To remedy this, we have *return* values (a.k.a. the output). A procedure can return a certain value(s), which can then be used in the rest of the program. Our procedure returns two things:
	* The URL that was found
	* The location of the end quote (a marker for where to start searching from next)
	
###Using Procedures	

This procedure, if given this input:

	my_page = """
        <div id="top_bin"><div id="top_content" class="width960">
          <a class="email_link" href="http://mail.google.com" style="color: red;">Gmail</a>
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
	
would return this: `http://mail.google.com` and `130`, which is the first URL and the location of where we should start searching for the next one! As you can see, inputs and outputs are critical to programming. Here's a real-world example of how crazy they can be: [Stanford's self-driving car](https://www.youtube.com/watch?v=iNu3AwbTEQs#t=18).

But, how do we actually use the procedure? In our case, `get_next_target` needs one input, a string called "page". It also has return values, `url` and `first_url_end`. What we want to do is get those return values when we call the procedure. We can call it like this:

	# think of this as:
	# first_url, marker = url, first_url_end
	first_url, marker = get_next_target(my_page)
	
	print first_url
	
	>>> http://mail.google.com
	
	print marker
	
	>>> 130
	
What happened was that we called the procedure `get_next_target`, so the interpreter jumps into that procedure to execute its code before continuing. Since the procedure returned two values, we were able to access them by assigning the values to `first_url` and `marker`.

Here's another, simpler example of a procedure called `sum`:

	def sum(a, b):
		return a + b
		
	c =  sum(1,2)
	print c
	
	>>> 3
	
Remember how variables used within procedures can't be accessed by the rest of the program unless they are returned? Here's an example illustrating that:

	def bad_sum(a, b):
		a = a + b
		
	a = 1
	b = 2
	
	bad_sum(a,b)
	
	print a
	
	>>> 1
	
On first glance, it might be assumed that calling `bad_sum` would change the value of `a` to be `a + b`. That is true, but only in the [*scope*](https://www.inkling.com/read/learning-python-mark-lutz-4th/chapter-17/python-scope-basics) of the procedure itself. What that means is that the `a` we defined outside of the procedure and set to equal 1 will still be 1 after we call `bad_sum`. What that essentially means is that `bad_sum` does nothing when called. Let's illustrate this:

	def bad_sum(a, b):
		print "bad_sum has been called!"
		a = a + b
		print "\tvalue of a within bad_sum: " + a
		
	a = 1
	b = 2
	
	print "value of a before calling bad_sum: " + a
	print "return value of sum: " + bad_sum(a,b)
	print "value of a after calling bad_sum: " + a
	
	
	>>> value of a before calling bad_sum: 1
	>>> bad_sum has been called!
	>>>     value of a within bad_sum: 3
	>>> return value of sum: None
	>>> value of a after calling bad_sum: 1
	
Notice that `None` in there? That means the absence of any value, a.k.a. nothing. And "nothing" is exactly what `bad_sum` does (and returns).

For our `bad_sum` procedure to be worth anything, it needs to have a return value that we can use.