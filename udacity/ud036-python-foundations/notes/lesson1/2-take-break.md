#Programming Foundations with Python

**Udacity: UD036**

---

###Project 1: Take a Break

Do you often spend too much time working at a computer? Let's write a program that schedules breaks for you throughout the day!

We are going to build the program right away, so let's plan things out first. There are many ways to go about solving this problem. Here's how we will do it:

We're going to write a program that keeps track of time, and does nothing until a certain amount of time has passed. It's execution steps will be:
	
1. Wait for 2 hours
2. Open up the web browser, which plays a video reminding us to take a break
3. Repeat these two steps indefinitely

While the steps themselves may seem pretty straightforward, one question that jumps to mind is how we will open the web browser using Python.

###Using Documentation

Since this is not immediately obvious, let's do a quick search for it on Google. Type "how to open web browser in Python 2" and hit Enter to get started.

The first link that should show up will be from the official Python docs, where all of the built-in Python classes and operators are documented. [Here's the link](https://docs.python.org/2/library/webbrowser.html), in case you can't find it.

Looking around will lead us to this documentation:

	webbrowser.open(url, new=0, autoraise=True)

		Display url using the default browser. If new is 0, the url is opened in the same 		browser window if possible. If new is 1, a new browser window is opened if 		possible. If new is 2, a new browser page (“tab”) is opened if possible. If 		autoraise is True, the window is raised if possible (note that under many window 		managers this will occur regardless of the setting of this variable).

		Note that on some platforms, trying to open a filename using this function, may 		work and start the operating system’s associated program. However, this is neither 		supported nor portable.

		Changed in version 2.5: new can now be 2.
	
This should fit our needs perfectly, and also demonstrate the power of being able to find things quickly using the internet. There's a lot to every programming language, so being able to read the documentation and know what you need is a critical skill to develop.

###Opening the Web Browser

Create a file called `take_break.py`, and put this into it:

	import webbrowser
	
	url = 'http://google.com/'
	
	webbrowser.open(url)
	
Assuming everything worked properly, you should see your default browser (Chrome in my case) open up and navigate to that page. We're well on our way to finishing our program!

Before we move on, notice how annoying it would be to have to type `webbrowser` every time we want to use it. Python's `as` keyword let's us get around that. Below is the same program, with a custom name I've given to the `webbrowser` module:

	import webbrowser as wb
	
	url = 'http://google.com'
	
	wb.open(url)
	
Nice!

###Making Our Program Wait

Now that we can open a URL in our browser, we need to move on to another piece of "Take a break": making the program wait a certain amount of time. Speaking of time, Python conveniently has a `time` module that can take care of this for us (like before, we can find out about stuff like this with a quick Google search).

Let's make our program wait 10 seconds (just so we can test it quickly):

	import time, webbrowser
	
	url = 'http://google.com'
	
	time.sleep(10)
	webbrowser.open(url)
	
Now we just need to wrap this in a loop and we're done with Project 1!

	import time
	import webbrowser as wb
	
	url = 'http://google.com'
	hours = 2 * 60 * 60 # two hours
	
	for i in range(0, 5):
		time.sleep(hours)
		wb.open(url)
		
We made it! Now, let's talk more about those Python modules that we imported, and how imports work.

###Python Standard Library

Imagine that the Python we downloaded is a file cabinet. This file cabinet, which we will call the "Python standard library", contains a bunch of files (who would've guessed). `webbrowser` and `time` happen to be two of those files, and they contain the code for functions like `open` and `sleep` that we used. They make our life easier, and are no different from the Python code we've been writing. In fact, you can write your own modules to import too (but that's beyond the scope of this class).

![Python std library](../img/stdlib.png)

What's nice about being able to import files like `webbrowser` and use it to open a URL in one line is that all of the implementation details are hidden from us. In other words, we don't need to know *how* `open` works, we just need to use it to serve our purpose.

This practice of hiding implementation details is called *abstraction*, and it allows us to spend more time on the program we want to write.

There's a ton of code in the Python standard library; read all about what's in it [here](http://docs.python.org/2/library/), as it is very well documented.

###Enhancing "Take a Break"

At this point, we've actually covered a lot, despite only writing a few lines of code. You can now:

* Use the internet and the Python docs to help you write programs
* Import modules and use them
* Write basic Python programs

As an optional side project, enhance your "Take a break" program to do something cool. Here's what I did with mine:

	import webbrowser as wb
	import time as t
	import sys

	def is_int(s):
		try:
			int(s)
			return True
		except ValueError:
			return False
    
    interval = int(sys.argv[1]) if len(sys.argv) > 1 and is_int(sys.argv[1]) else 300
    url = sys.argv[2] if len(sys.argv) > 2 else 'http://xkcd.com/'

	for i in range(0,5):
		t.sleep(interval)
		print t.asctime()
		wb.open(url)
	
I decided to learn about the `sys` module, which let's me get optional arguments from the command line. So, running my program like this:

	python take_break.py 300 http://yoututbe.com
	
would tell it to wait 300 seconds before opening YouTube in the browser.