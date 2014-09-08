#Programming Foundations with Python

**Udacity: UD036**

---

###Lesson 3: Making Classes

Now that we know how classes work and how to use them, it's time for us to progress towards making our movie website by learning how to create our own classes.

**Planning our Movie Website**

Here's how our movie website will function:

1. Go to the website
2. See all of the movies displayed
3. Click on one to play it's trailer

It's pretty simple in terms of concept, but how about implementation?

**Class structure**

We will need classes to build this movie website. Recall how classes are like blueprints, and that we can make several instances of a class. We want our `Movie` class to be a template for a generic movie, and then create instances of that class like this:

	toy_story = Movie()
	
and add details to each specific movie. So, we first need to come up with a list of properties that we think every movie should have:

* title
* trailer
* storyline
* poster_image
* reviews

We will leave out some things like cast and box office numbers, since the things we listed above will be enough to get started. As far as methods we need to write, for now let's focus on:

* `show_trailer()`

**Defining our class**

Create a new file, called `media.py`. Inside of it, start our `Movie` class by typing:

	class Movie():
	
Notice how the "M" is uppercase? This is not necessary, but is considered good practice. For more on Python best practices and style guidelines, read [this document](http://google-styleguide.googlecode.com/svn/trunk/pyguide.html). Best practices and standards are important to making sure that programmers all over the world can easily understand each other's code!

Let's stop with what we have for now and try to create an instance of the class `Movie` in another file. Create a second file, called `media_center.py` and type this:

	import media # the file we made
	
	toy_story = media.Movie()
	
Looks good! Or does it? We're forgetting something important. When we did this before:

	joe = turtle.Turtle()
	
What was happening behind the scenes was that a function named `__init__` was being called. This function creates a new instance of the class by creating space in the computer's memory for that instance.

We need that function for our `Movie` class too! Note that another word for that `__init__` function is the *constructor*, since it "constructs" an instance of our class. Before we begin, you may be wondering what the deal is with the two underscores before and after the name "init". It's just a convention, actually: Python leads and follows names it doesn't want to conflict with user defined variables and functions with two underscores. More about that can be [found here](http://stackoverflow.com/questions/1301346/the-meaning-of-a-single-and-a-double-underscore-before-an-object-name-in-python).

Let's define `__init__`. It will be defined like any other function in Python, with one small difference: we need to pass in the word `self`, which is a reference to the object being created (in one case, that could be `toy_story`), as the first parameter.

**Note**- Using `self` is simply convention; here's an excerpt from the Python docs explaining it:

	Often, the first argument of a method is called self. This is nothing more than a convention: the name self has absolutely no special meaning to Python. Note, however, that by not following the convention your code may be less readable to other Python programmers, and it is also conceivable that a class browser program might be written that relies upon such a convention.
	
Here's our new class:

	class Movie():
		def __init__(self, title, storyline, poster_image_url, trailer_youtube_url):
			self.title = title
			self.storyline = storyline
			self.poster_image_url = poster_image_url
			self.trailer_youtube_url = trailer_youtube_url
			
Let's stop and take a step back for a second. A lot of this may look pretty odd, for example, this new `self.thing` syntax. What we are doing is passing in 4 pieces of information to the `__init__` function, and then setting those to things called *instance variables*. So, when we pass in a title, and assign its value to `self.title`, we are saying "this movie's title is the title we passed in". This will make a lot more sense in a second.

Go back to our other file:

	import media
	
	toy_story = media.Movie("Toy Story", "A story of a boy and his toys that come to life", "http://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg", "https://www.youtube.com/watch?v=KYz2wyBy3kc")
	
	print toy_story.title
	
	>>> "Toy Story"
	
	print toy_story.storyline
	
	>>> "A story of a boy and his toys that come to life"
	
Does everything make sense now? When we said `self.title = title` back in our `__init__` function, and passed in "Toy Story" when we created an instance of `Movie`, we were saying "set the title of the Movie toy_story to Toy Story".

**What's going on behind the scenes**

When we run this code:

	toy_story = media.Movie("Toy Story", "A story of a boy and his toys that come to life", "http://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg", "https://www.youtube.com/watch?v=KYz2wyBy3kc")
	
several things happen.

1. `__init__` gets called
2. All references to `self` inside of `__init__` point to `toy_story`
3. The variables associated with the instance `toy_story` get assigned values:
	* `toy_story.title` becomes "Toy Story"
	* `toy_story.storyline` becomes "A story of a boy and his toys that come to life"
	* etc...
	
**Creating more movies**

Let's make some more movies:

	avatar = media.Movie("Avatar",
						"A marine on an alien planet",
						"http://upload.wikimedia.org/wikipedia/en/b/b0/Avatar-Teaser-Poster.jpg",
						"https://www.youtube.com/watch?v=cRdxXPV9GNQ"
	)
	
Now we know what is happening when we create an instance of `Movie`!

###Showing Trailers

It's time to define our `show_trailer` method. We will want do define this inside of the `Movie` class. Methods defined inside of a class are called *instance methods*. Let's get coding:

	import webbrowser as wb

	class Movie():
		def __init__(self, title, storyline, poster_image_url, trailer_youtube_url):
			self.title = title
			self.storyline = storyline
			self.poster_image_url = poster_image_url
			self.trailer_youtube_url = trailer_youtube_url
			
		def show_trailer(self):
			wb.open(self.trailer_url)
			
Notice that we had to pass `self` in again; this is true of all instance methods. Let's modify our other file a bit to see things working:

	import media
	
	toy_story = media.Movie("Toy Story", "A story of a boy and his toys that come to life", "http://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg", "https://www.youtube.com/watch?v=KYz2wyBy3kc")
	
	toy_story.show_trailer()
	
Run it, and your web browser should open with the trailer playing! We're making good progress.

###A Quick Recap

Here's the vocabulary we've learned so far, summarized in a picture:

![vocab](../img/vocab.png)

###Creating the Movie Website

Now that we have a class definition and the only method we need, let's make our website! First, let's define a few more movies for our site:

	 toy_story = media.Movie("Toy Story", "A story of a boy and his toys that come to life", "http://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg", "https://www.youtube.com/watch?v=KYz2wyBy3kc")
	 
	 avatar = media.Movie("Avatar", "A marine on an alien planet", "http://upload.wikimedia.org/wikipedia/en/b/b0/Avatar-Teaser-Poster.jpg", "https://www.youtube.com/watch?v=cRdxXPV9GNQ")
	 
	 school_of_rock = media.Movie("School of Rock", "Jack Black is not a good actor", "http://upload.wikimedia.org/wikipedia/en/1/11/School_of_Rock_Poster.jpg", "https://www.youtube.com/watch?v=XCwy6lW5Ixc")
	 
	 hunger_games = media.Movie("Hunger Games", "Children participate in death match", "http://upload.wikimedia.org/wikipedia/en/4/42/HungerGamesPoster.jpg", "https://www.youtube.com/watch?v=keT5CRhhy84")
	 
You can define more if you want, but this will be enough to work with. We will also need the code for the website itself (since this isn't a web programming course and we aren't going to make it ourself), which can be found [here](https://s3.amazonaws.com/udacity-hosted-downloads/ud036/fresh_tomatoes.py).

We're going to use this file (called `fresh_tomatoes.py`) in our own media center code. Let's create a list of movies that we are going to use:

	import fresh_tomatoes

	movies = [toy_story, avatar, school_of_rock, hunger_games]
	fresh_tomatoes.open_movies_page(movies)
	
Running that file will give us our website! Although there may seem to be a bit of "magic" with how we went from defining a simple class to a fully functioning website, that's okay; the point of the project was not to develop a website (that's what CS 253 is for!), but to simply show how object-oriented programming can make life easier!