#Intro to Computer Science

**Udacity: CS 101**

---

###Admiral Grace Hopper (1906-1992)

> "Nobody believed that I had a running compiler and nobody would touch it. They told me computers could only do arithmetic." - Grace Hopper

Grace Hopper was a pioneer of computer science, and a rear admiral in the US Navy. Some of her accomplishments and advancements include:
	
* Writing the first compiler for a language, leading to the development of [COBOL](http://www.csis.ul.ie/cobol/course/Default.htm)
* Popularizing the idea of machine-independent programming languages
* Creating the term "debugging" (inspired by an actual moth in her computer)

###Variables

Clearly, computers can do more than just arithmetic, as Grace Hopper proved. We can use something called a *variable* to store and manipulate values. Variables have names, and have values assigned to them like this: `name = value`.

For example, in Python:

	# here, we are creating a variable called speed_of_light and
	# assigning the value of 299792458 to it.
	speed_of_light = 299792458
	
We can then use that variable to make our programs more readable:

	speed_of_light = 299792458
	billionth = 1.0 / 1000000000
	nanostick = speed_of_light * billionth * 100
	
	print nanostick
	
NOTE: The "=" sign does not mean "equals" in most languages. It is the *assignment* operator, which says: "The value of the name on the left side will be the value on the right".

Here's another example of variables in use:

	# what is the value of seconds after running this code?
	minutes = minutes + 1
	seconds = minutes * 60
	
The correct answer is *nothing*. An error will be thrown because we never set an initial value to `minutes` before trying to access its value in the first line.

In Python, the error would look something like this:

	Traceback (most recent call last):
		File "<stdin>", line 2, in <module>
	NameError: name 'minutes' is not defined
	
###Strings

A computer can be much more than the simple calculator we have been using it as thus far.

We have only been dealing with numbers, like 0 and 29.785. Not all data is in numeric form, so let's learn about another data type: the *string*.

A string is just a sequence of characters. In Python, they look like this:

	my_string = "Hello"
	
or

	my_string = 'Hello'
	
If we start with a single-quote, we need to end with a single-quote, etc. Which means this is legal as well:

	# note the use of a single quote inside a double-quoted string
	sentence = "And I think it's gonna be a long, long time..."
	
We can also have multiline strings in Python! Check out this poem:

	"""
	There is a place where the sidewalk ends
	And before the street begins,
	And there the grass grows soft and white,
	And there the sun burns crimson bright,
	And there the moon-bird rests from his flight
	To cool in the peppermint wind.

	Let us leave this place where the smoke blows black
	And the dark street winds and bends.
	Past the pits where the asphalt flowers grow
	We shall walk with a walk that is measured and slow,
	And watch where the chalk-white arrows go
	To the place where the sidewalk ends.

	Yes we'll walk with a walk that is measured and slow,
	And we'll go where the chalk-white arrows go,
	For the children, they mark, and the children, they know
	The place where the sidewalk ends.
	
	-Shel Silverstein
	"""

###Using Strings

**Concatenation**

We can still perform operations on strings, even though they aren't numbers. Check out *concatenation* in Python:

	first_name = 'Bob'
	last_name = 'Johnson'
	name = first_name + ' ' + last_name # note use of space
	print name
	
	>>> Bob Johnson
	
We can't concatenate strings and numbers in Python:

	name = 'Dave'
	age = 40
	
	print name + " is " + age + " years old."
	
	>>> Traceback (most recent call last):
			File "<stdin>", line 4, in <module>
		TypeError: unsupported operand type(s) for +: 'int' and 'str'
		
But we can *multiply* a string:

	print "Ty" * 5
	
	>>> TyTyTyTyTy
	
**Indexing Strings**

The characters in a string are *indexed* starting at 0:

	Character: U d a c i t y
	Index:     0 1 2 3 4 5 6
	
In Python, we can access these individual characters like this:

	company = "Udacity"
	first_letter = company[0] #index 0 of company
	
	print first_letter
	
	>>> U
	
Using negative numbers starts at the last character of the string:

	last_letter = company[-1]
	
	print last_letter
	
	>>> y

Make sure you don't try to access something not in the string's range, or else we may get an error like this:

	name = 'Dave'
	print name[12]
	
	>>> Traceback (most recent call last):
			File "<stdin>", line 2, in <module>
		IndexError: string index out of range
		
Index values can include operations inside of them: `s[3]` is exactly the same as `s[1 + 1 + 1]` and `s[2 * 2 - 1]`.

**Sub-sequences of strings**

What if we wanted to take a string and grab a piece of it? We can do that like this in Python:

	me = 'Robert'
	nickname = me[0:3] #first value is inclusive, second one is not
	
This is the same as:

	me = 'Robert'
	nickname = 'Rob'
	
and:

	me = 'Robert'
	nickname = me[0] + me[1] + me[2]
	
Leaving the spot before or after the colon empty does something cool:

	me = 'Robert'
	print me[:3]
	
	>>> Rob
	
	print me[3:]
	
	>>> bert
	
	print me[:] #not useful but behaves as expected
	
	>>> Robert
	
**Finding strings within strings**

Python's `find()` method (a built-in procedure provided by Python; more on these soon) allows us to grab a sub-string within an input string. It works like this:

`search_string.find(target_string)`

If the target string is found, the output we get is the index within the first string, where the target string begins. For example:

	search_string = "I am a happy man."
	target_string = "am"
	
	print search_string.find(target_string)
	
	>>> 2
	
We get `-1` as an output if the target string is not found. In the case that the target string is found *more than once*, the output will always be the *first* instance.

NOTE: `find()` is case sensitive! To ignore case before calling `find()`, we can do something like this:

	search_string = "I am a happy man."
	target_string = "Am"
	
	print search_string.find(target_string.lower())
	
	>>> 2
	
**Finding with numbers**

What if we want to find more than just the first occurrence of a substring? We can do this by passing in a second parameter to `find()`, which is the start position:

	search_string = "I am a happy man, I promise I really am."
	target_string = "am"
	
	print search_string.find(target_string, 10)
	
	>>> 37
	
Notice how the first occurrence was skipped, because we started at `search_string[10]`. We now know enough to solve some bigger problems:

###Extracting Links from Web Pages

Let's put all of these string operations together to solve a problem: how can we extract links from a web page for our search engine?

**HTML Crash Course**

If you go to this [Wikipedia page](http://en.wikipedia.org/wiki/Robert_Louis_Stevenson), you'll notice tons of blue links everywhere. To understand how we can grab those for our web crawler, we need to first see how links work in [HTML](https://developer.mozilla.org/en-US/docs/Web/HTML), which is the tempting language of the web. This is a section of that Wikipedia page's HTML:

	<p>Half of Stevenson's original manuscripts are lost, including those of <i><a href="/wiki/Treasure_Island" title="Treasure Island">Treasure Island</a></i>, <i><a href="/wiki/The_Black_Arrow" title="The Black Arrow" class="mw-redirect">The Black Arrow</a></i> and <i><a href="/wiki/The_Master_of_Ballantrae" title="The Master of Ballantrae">The Master of Ballantrae</a></i>. Stevenson's heirs sold Stevenson's papers during World War I; many Stevenson documents were auctioned off in 1918.<sup id="cite_ref-76" class="reference"><a href="#cite_note-76"><span>[</span>76<span>]</span></a></sup></p>
	
While this isn't pretty to look at, you may notice a structure to everything. While this is not the place to learn about HTML or web design (try [this course](http://www.codecademy.com/en/tracks/web) if interested), here are some basics:

* HTML is based on a system of *tags*, which can look like this:
	* Non-block elements
		* `<img>` (notice the lack of a closing tag for non-block elements)
		* `<hr>`
	* Block elements
		* `<div></div>`
		* `<a></a>`
* Tags have *attributes*, and each attribute, like a Python variable, has a *value*:
	* Take this image tag for example:
		* `<img src="http://placekitten.com/400/400">`
			* The `src` (source) attribute has the value of [http://placekitten.com/400/400](http://placekitten.com/400/400), meaning that the location of the image is that URL.

		
For the purposes of this project, all that we care about are *link* tags, represented by `<a></a>`. Generally, a link looks like this:

	<a href="http://placekitten.com/400/400">placeholder cat image</a>

The `href` attribute, like `src` for images that we saw earlier, tells us where the link points to. Were I to click on that link in a web page, I would be taken to a page with something like this on it:

![kitten](http://placekitten.com/400/400)

To build the crawler, we need to keep track of and follow all of the links on a web page. We need to do this:

1. Get the HTML that comes back from an [HTTP request](http://www.jmarshall.com/easy/http/). This is our "seed page".
2. Find all of the link tags. (Not all web pages will have them, for future reference)
3. Grab the value inside of the `href` for each link and store it.
4. Repeat for every page, until we reach dead ends and cannot continue.

Let's move on!