#Programming Foundations with Python

**Udacity: UD036**

---

###Mini-Project: Profanity Checker

Now that we understand how to use classes and a bit on how they work, let's make one last project: a program that will read text and tell us if there is profanity in that text.

**Planning things out**

Here are the steps I would take to write our profanity checker program:

1. Read the text from a file
2. Check the text for curse words
3. Notify the user if there are curse words found

To get started, create two text files, one with profanity and another without it.

**Reading from files**

Reading from files couldn't be simpler in Python! All we have to do to open a file for reading (not writing) is call the `open` operator, and grab the text with `read()`. No imports needed to do that, so if we had to give `open` and `read` a place in the Python standard library, it'd be directly inside it, rather than inside a module like `os` or `webbrowser`. Here's a program that can read files:

	import os

	def read_text(path_to_file):
		quotes = open(path_to_file)
		content = quotes.read()
		quotes.close() # good practice to "close" a file when you're done
		return content

	files = ['files/' + f for f in os.listdir('files')]

	for f in files:
		text = read_text(f)
		check_profanity(text) # not implemented yet
		
We're already most of the way there, as we can read text from a file. For more on opening, reading from, and writing to files, check out [the docs](https://docs.python.org/2/library/stdtypes.html#bltin-file-objects). 

What `open` does is return an "object" of the file type. Sound familiar? When we say `quotes = open(path_to_file)`, it's the same as when we called `turtle.Turtle()` from before: we are creating an instance of the `File` class. Therefore, `__init__` is still called! We will get to stuff like this later in the course more.

For right now though, how will we check for profanity?

**Checking for profanity**

We could, with some trouble, try to create a list of every curse word in our program. However, this would take unnecessary amounts of time, probably not be complete, and we wouldn't really gain anything from doing that.

So, let's use a third-party tool (like we did with Twilio). We don't need to import or download anything this time though, because we're just going to use a nice and simple API available for free online.

If you go to this URL: `http://www.wdyl.com/profanity?q=hello`, you'll see something like this:

	{"response": "false"}
	
That's a simple JSON object (more about JSON [here](http://json.org/)) which probably looks familiar if you're used to Python dictionaries. It's telling us that our query string, which was "hello" in the above example, contains no profanity. Just what we need!

But, how do we use this website from inside our code? We can import a module called `url lib`, as it turns out. Let's see it in use:

	def check_profanity(text_to_check):
		connection = urllib.urlopen('http://www.wdyl.com/profanity?q=' + text_to_check)
		response = connection.read()
		print response
		connection.close()
		
All we are doing is connecting to the website by passing in a URL, and getting the response. Pretty easy! Let's finish up this program:

	import os, urllib

	def read_text(path_to_file):
		quotes = open(path_to_file)
		return quotes.read()

	def check_profanity(text_to_check):
		url = 'http://www.wdyl.com/profanity?q=' + text_to_check
		connection = urllib.urlopen(url)
		response = connection.read()
		connection.close()
		return True if 'true' in response else False

	files = ['files/' + f for f in os.listdir('files')]

	for f in files:
		text = read_text(f)
		has_swears = check_profanity(text)
		if has_swears:
			print "File: " + f + " contains profanity!"
			
We're all done! Running this code on a file with profanity should give an output like this:

	File: files/yes.txt contains profanity!
	
###Summary

We've now, at this point, successfully used a bunch of classes and Python modules! We:

* Wrote a program to tell us when to take a break
* Played around with Turtle graphics to learn about classes
* Sent text messages from our code with Twilio
* Used the `File` class, `urllib`, and an API to check for profanity in text

Time to make our own classes!