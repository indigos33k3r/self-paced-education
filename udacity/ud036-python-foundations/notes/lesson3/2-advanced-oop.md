#Programming Foundations with Python

**Udacity: UD036**

---

Now that we can use classes, and make our own, let's move on to some more advanced OOP ideas.

###Class Variables

Recall the *instance* variables that we used in our `Movie` class. These included things like the title, trailer, etc. They're called instance variables because their values are unique to each instance of the class.

That means that when I create a movie called `toy_story` and set its name to "Toy Story", another movie called `avatar` can't access `toy_story`'s name.

Sometimes, however, we want variables that *all* of our instances can share. These types of variables are class variables. Here's an example that relates to the movie project:

Let's say we wanted to have a variable to store all of the valid movie ratings:

	ratings = ['G', 'PG', 'PG-13', 'R']
	
This is obviously something we want to be able to share across all instances of `Movie`, rather than pass it in every single time we create a movie. Here's how we do that, and it's actually very simple:
	
	import webbrowser as wb

	class Movie():
		
		ratings = ['G', 'PG', 'PG-13', 'R']
		
		def __init__(self, title, storyline, poster_image_url, trailer_youtube_url):
			self.title = title
			self.storyline = storyline
			self.poster_image_url = poster_image_url
			self.trailer_youtube_url = trailer_youtube_url

		def show_trailer(self):
			wb.open(self.trailer_youtube_url)
			
Easy as that! If we want to access that variable, we could do so from any instance of the `Movie` class:

	print toy_story.ratings
	
	>>> ['G', 'PG', 'PG-13', 'R']
	
###Doc Strings

All classes in Python come with some existing class variables. Let's talk about one of them, `__doc__`.

This variable is used to provide documentation for a class. We can see one in action like this. Start up an interactive Python shell (by typing 'python' into your terminal):

	import turtle
	
	turtle.Turtle.__doc__
	
	>>> 'RawTurtle auto-creating (scrolled) canvas.
		When a Turtle object is created or a function derived
		from some Turtle method is
		called a TurtleScreen object is automatically created.'
		
Cool! Let's add documentation to our `media.Movie` class by simple adding this at the top of the class definition:

	"""Provides a way to store movie information"""
	
The triple quotes allow us to split a string up into multiple lines (we don't need to here though). Now, try running this:
	
	import media

	print media.Movie.__doc__
	
	>>> Provides a way to store movie information
	
This can be very useful, especially with complicated classes. There are other pre-defined variables like `__doc__` too, so read about them [here](http://www2.lib.uchicago.edu/keith/courses/python/class/5/).

###Inheritance

As you probably know, children can inherit the traits of their parents, like eye color, etc. There is a similar concept in OOP that works the same way. Let's say we had two classes, `Parent` and `Child`.

Here's the instance variables that `Parent` has:

* last name
* eye color

And for `Child`:

* number of toys

Let's turn this into code. Create a file called "inheritance.py" to get started:

	class Parent():
		def __init__(self, last_name, eye_color):
			print "Parent constructor called"
			self.last_name = last_name
			self.eye_color = eye_color
			
	bob = Parent('Jones', 'blue')
	
	print bob.last_name
	
	>>> Parent constructor called
	>>> Jones
	
This works! The reason we printed when the `__init__` function was called will become clear soon. Let's make a class `Child` now, and something will look a bit different:

	class Child(Parent):
		def __init__(self, last_name, eye_color, num_toys):
			print "Child constructor called"
			Parent.__init__(self, last_name, eye_color)
			self.num_toys = num_toys
			
This may look funny, but it's pretty logical: `Child` inherits a few variables from `Parent`, so we are going to let the `Parent` constructor take care of those shared variables. We can then extend the functionality offered by the `Parent` constructor to handle the extra variable, `num_toys`.

Let's put our code together to see how it all works:

	class Parent():
		def __init__(self, last_name, eye_color):
			print "Parent constructor called"
			self.last_name = last_name
			self.eye_color = eye_color
		
	class Child(Parent):
		def __init__(self, last_name, eye_color, num_toys):
			print "Child constructor called"
			Parent.__init__(self, last_name, eye_color)
			self.num_toys = num_toys
		
	print "Creating bob..."		
	bob = Parent('Jones', 'blue')
	
	print "Creating joe..."
	joe = Child('Jones', 'green', 5)
		
The output of this code would look something like this:

	Creating bob...
	Parent constructor called
	
	Creating joe...
	Child constructor called
	Parent constructor called
	
Inheritance works for two reasons:

1. It is easy to conceptualize: it makes sense why `Child` would inherit from `Parent`, or perhaps why `Visa` could inherit from a `CreditCard` class, etc.
2. We get to re-use code instead of writing it all again.

###Back to the Movies

With our new inheritance knowledge ready to use, let's update the design of `Movie`. What if we wanted to create another class, called `TVShow`? As you might imagine, it will have some new attributes:

* season
* episode
* station

And perhaps a new method:

* get_local_listing()

But, it may also share some things with `Movie`, such as having a storyline and a title. Is there any way we can use inheritance to help here, so we don't write redundant code?

Let's start by thinking about a *superclass* of `Movie` and `TVShow`, much like `Parent` was to `Child`. It could be called `Video`, and have instance variables for `title` and `storyline`, which `Movie` and `TVShow` would then inherit. While we won't implement it right now, hopefully you can see why it would be helpful, especially if we started adding other types of media as well, like `MusicVideo` or `Documentary`, etc.

###Reusing Methods

Let's go back to our `Parent` and `Child` code, and add a method called `show_info` to `Parent`:

	class Parent():
		def __init__(self, last_name, eye_color):
			print "Parent constructor called"
			self.last_name = last_name
			self.eye_color = eye_color
		
		def show_info(self):
			print 'Last Name: ' + self.last_name
			print 'Eye Color: ' + self.eye_color
	
	class Child(Parent):
		def __init__(self, last_name, eye_color, num_toys):
			print "Child constructor called"
			Parent.__init__(self, last_name, eye_color)
			self.num_toys = num_toys
		
Since `Child` inherits from `Parent`, we can actually use this method on both an instance of `Parent` or `Child`:

	bob = Parent('Jones', 'blue')
	joe = Child('Jones', 'green', 5)
	
	bob.show_info()
	joe.show_info()
	
The output would look as expected:

	Last Name: Jones
	Eye Color: blue
	
	Last Name: Jones
	Eye Color: green
	
###Overriding Methods

Being able to reuse methods is great, but you may have noticed that we weren't able to print the number of toys that Joe had by using `Parent`'s `show_info` method. This is where overriding comes in handy.

Let's simply redefine `show_info` for `Child`:

	class Child(Parent):
		def __init__(self, last_name, eye_color, num_toys):
			print "Child constructor called"
			Parent.__init__(self, last_name, eye_color)
			self.num_toys = num_toys
			
		def show_info(self):
			print 'Last Name: ' + self.last_name
			print 'Eye Color: ' + self.eye_color
			print 'Number of Toys: ' + self.num_toys
			
And we could then call the method on an instance of `Child` to get all of the information!

###Final Project

Now that we know how to use modules, use classes, and even create our own classes, let's attempt to make a project of our own! A detailed description of the project can be found [here](https://docs.google.com/document/d/1-TKicJNzRO4ftAKZHbXCBbGSfRI6RszAu-OOtJW7CLg/pub).

Basically, we are going to have some freedom and fun with this project. There are 3 main steps:

1. Come up with an idea for the project
2. Design a solution (written out, not code)
3. Program the project

In the `code` folder, I have provided my own solution for a final project: a command-line interface for managing contacts in a database. Be sure to come up with your own though, and use what we learned in this class!