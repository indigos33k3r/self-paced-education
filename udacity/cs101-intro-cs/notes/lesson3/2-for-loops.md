#Intro to Computer Science

**Udacity: CS 101**

---

###Loops and Lists

Remember the `while` loop? They're used for doing things over and over again, as long as a condition is true. Here's an example:

	i = 0
	while (i < 10):
		print i
		i = i + 1
	
	print "we aren't in the loop anymore!"
	
The above code would print the value of `i` (initially set to 0), increment it by 1, and go back to the start of the loop until i was no longer less than 10. Now that we know about lists, let's use a `while` loop with a list:

	def print_list(p):
		i = 0
		while i < len(p):
			print p[i]
			i += 1
			
This procedure is pretty simple; it prints all of the items in a given list.

**For loops**

The `for` loop is another type of loop, that is very useful for iterating over some data structure (like a list), because iteration is taken care of for us. They work like this:

	for item in list:
		do something
		
Here's the `print_list` procedure, except with `for` loops:

	def print_list(p):
		for item in p:
			print item
	
A little nicer, right? For each iteration of the loop, the index of the list that `item` refers to is incremented by 1, until we have gone through all of the elements in the list.

Here's another example of `for` loops in action:

	# Define a procedure, measure_udacity,
	# that takes as its input a list of strings,
	# and returns a number that is a count
	# of the number of elements in the input
	# list that start with the uppercase 
	# letter 'U'.

	def measure_udacity(p):
		c = 0
    		for e in p:
         	c += 1 if e[0] == 'U' else c
     	return c

	print measure_udacity(['Dave','Sebastian','Katy'])
	#>>> 0

	print measure_udacity(['Umika','Umberto'])
	#>>> 2
	
`for` loops are fairly simple, but incredibly useful. We will be applying them to our search engine shortly! You may have noticed this weird line in the code above:

	c += 1 if e[0] == 'U' else c
	
Luckily, it's pretty readable; in English, it would read something like "Increment c by 1 if the first letter in the string is 'U', and otherwise keep it the same".

It's essentially just a regular `if` block, just written out in one line. In fact, the entire method can be written in one line:

	def measure_udacity(p):
		return sum(e[0] =='U' for e in p)
		
Again, this code is probably foreign, but still relatively readable even if you haven't seen it before. It does the same thing as before, just all neatly packed into one line. For more on this style of programming in Python, read [this tutorial](https://docs.python.org/2/tutorial/datastructures.html#list-comprehensions)!

**Index**

A useful list operation that comes in handy when dealing with lists is the `index` method. It works like this:

	p = [0,1,2]
	
	print p.index(1)
	
	>>> 1
	
	print p.index(22)
	
	>>> ValueError: 10 is not in list
	
Very simple, and very useful. Not convinced? Let's try to write a procedure, called `find_element`, which will return the location of an element `t` in a list `p`, or -1 if the item is not in the list. First, without using `index`:

	def find_element(p, t):
		i = 0
		for e in p:
			if e == t:
				return i
			i += 1
		return -1
		
This works, but `index` can help us shorten it up a lot:

	def find_element(p, t):
		return p.index(t) if t in p else -1
		
If you don't like the one-liner, we can expand it as:

	def find_element(p, t):
		if t in p:
			return p.index(t)
		return -1
		
**Pop**

`pop` is another list operation that will be very useful in building our web crawler. The way it works is by:

1. Removing the final element in a list
2. Returning that removed value

Here's `pop` in action:

	a = [1, 2, 3]
	b = a
	
	x = a.pop()
	
	print x
	
	>>> 3
	
	print a
	
	>>> [1, 2]
	
	print b
	
	>>> [1, 2]