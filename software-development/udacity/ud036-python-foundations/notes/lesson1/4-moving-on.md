#Programming Foundations with Python

**Udacity: UD036**

---

###When Functions Don't Suffice

Our next big project is to write a movie database, in the style of [IMDB](http://www.imdb.com/). We could do this using only what we know so far, so let's get started.

A movie has a lot of data associated with it; things like title, storyline, actors and actresses, etc. We also want to be able to *do things* with our movies, so we will need functions to play the trailers, and other things like that. Some basic functions could look like this:

	def show_trailer(title, url):
		# open browser and play trailer
		
	def show_info():
		# print movie information
		
Notice that I left the parameters empty for `show_info`? That's because what we need to pass in is not so obvious unfortunately, and also not that fun. Since we can have an unlimited number of movies, TV shows, etc, all with different information, having one function to do everything is difficult. So, we'd need to pass in *all* of the information we want displayed, *every single time* we call the procedure. Here's a sad example:

	show_info("Toy Story", "http://youtube.com/trailer", "John Lasseter", 30000000, "Andy's Toys Come To Life", "May 22, 1995")
	
This is pretty ugly, and not sustainable, because different types of content have different types and amounts of data associated with them. What we want to do instead is supply a template that defines what a movie or TV show is in our code, and what attributes they have.

We want to be able to say "Toy Story is a movie" or "Avatar is a movie". We could do this by making a bunch of files called "toy_story.py" or "avatar.py", but as you might imagine, this approach isn't very scalable.

Our end goal is to be able to define one template, and use it multiple times without re-writing anything. This template is called a *class*, and we will learn about it next lesson.