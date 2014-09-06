#Intro to Computer Science

**Udacity: CS 101**

--

###The Web Crawler

**Getting the first link**

Let's start with getting the location of the first link on our "page" (which will be a string for simplicity):

	# Write Python code that initializes the variable
	# start_link to be the value of the position
	# where the first '<a href=' occurs in a page.

	page = '''
			<div id="top_bin"> <div id="top_content" class="width960">
			<div class="udacity float-left"> <a href="/">
		   '''

	start_link = page.find("<a href=")

This would give us the starting location of `<a href="/">`. We now need to extract the URL from that output. We can do this by getting the first double-quote that appears after the next `href` attribute, since it will belong to the `<a...` that we found.

Here is how we can extract the first link on any given HTML page (caution: this solution is a bit more complicated than necessary for where we are at right now):

	# Write Python code that assigns to the variable url a string that is the value 
	# of the first URL that appears in a link tag in the string page.
	# Your code should print http://udacity.com. Make sure that if page 
	# were changed to page = '<a href="http://udacity.com">Hello world</a>'
	# that your code still prints the same thing.

	# page = contents of a web page
	page = """
        <div id="top_bin"><div id="top_content" class="width960">
          <a class = "email_link" href="http://mail.google.com">Gmail</a>
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

This works well because it handles many cases. All of these link tags could be passed in and still have the URL extracted:

	<a href="http://udacity.com">Udacity</a>
	<a href='http://udacity.com'></a>
	<a class="link" href = "http://udacity.com">Udacity</a>
	<a href= "http://udacity.com">Udacity</a>
	
You may have noticed a few unfamiliar things in the above code; they will all be addressed more later on, but here's a brief introduction for now:

1. Lists
	* Lists are a very useful *data structure*. What is a data structure? It's exactly  what it sounds like: a structure for holding certain types of data. In this case, we're dealing with lists (which look like *arrays* for those familiar with another language). Lists in Python can hold any type of data, and are indexed just like strings. Here's an example of using lists:
	
			# here's a list that will hold some numbers
			favorite_numbers = [1, 34, 22]
			print favorite_numbers[0]
			
			>>> 1
			
			# lists can hold different types of data
			things = ["Hello World!", 300, 2.2, 'a']
2. `for` loops
	* Loops are used in many cases. Let's sat you have a set of data that you want to iterate over:
				
			# lets print the squares of every number in this list
			my_list = [0,1,2,3]
				
			# here's one way, not using loops
			print my_list[0]**2 #the ** operator is for exponents
			print my_list[1]**2
			print my_list[2]**2
			print my_list[3]**2	
		
			# the above is tedious, and would be impossible to scale
			# if we had a list that was 10000 items long, for example
			# this is where loops come in handy:
			
			for x in my_list:
				print x**2
				
			# this essentially says, for every value "x" in my_list,
			# print out its square
				
			# we can use for loops in many other ways, but that'll
			# be fine for our purposes right now

3. The `len()` method
	* This method is used, as the name suggests, to get the length of any object with a length property:
	
			# these will work
			print len([0,1,2])
			
			>>> 3
			
			print len("Hello") 

			>>> 5
			
			# these will not
			
			len(0)
			
			>>> TypeError: object of type 'int' has no len()
			
			len()
			
			>>> TypeError: len() takes exactly one argument (0 given)
			
4. The `.replace()` method
	* This method, which is for strings, takes two arguments: a value to find, and a value to replace it with. Check it out:
	
			sentence = "Hello, my name is Bob!"
			
			#replace() in action:
			new_sentence = sentence.replace("Bob", "Ty")
			
			print new_sentence
			
			>>> Hello, my name is Ty!
			
5. Conditional statements
	* You may have noticed this statement in the solution:
	
			if page[page.find("href=", first_link) + len("href=")] == '"':
				first_url = page[first_url_start:page.find('"', first_url_start)]
			else:
				first_url = page[first_url_start:page.find("'", first_url_start)]
				
	* It looks a bit complicated due to the length of it, so here's a simpler example:
	
			if (2 > 1):
				print "2 is greater than 1"
			else:
				print "1 is greater than 2. Uh oh, math is broken!"
				
	* Make sense? That's called a conditional block, a.k.a. an "if-else" statement. Translated to English, it would say: "If this condition is true, do this. Otherwise, do this." In our case, the condition is "2 > 1". Since this is true, the code above will result in this output:
	
			>>> 2 is greater than 1
			
It may seem like we covered a lot just to solve this one problem. There is a lot to Python, and a lot to programming in general. You won't always know the answer off the top of your head, so this is where the internet comes in handy. Here are some great resources to learn more about Python, and programming in general:

* [Stack Overflow](http://stackoverflow.com/): A Q&A site for programmers
* [The Python Documentation](https://docs.python.org/2/): The official docs for the language (Python 2) and its syntax
* [Online Python Tutor](http://pythontutor.com/): Visualize and execute Python code step-by-step