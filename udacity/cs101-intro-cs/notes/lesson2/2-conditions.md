#Intro to Computer Science

**Udacity: CS 101**

---

###Making Decisions

**Boolean values and comparison operators**

Python, and every other programming language, has a way of comparing two values. In Python, these are called *comparison operators*. Here are some of them:

* `<`: less than
* `>`: greater than
* `<=`: less than or equal to
* `>=`: greater than or equal to
* `==`: equal to (need two = signs since only one is reserved for assigning variables)
* `!=`: not equal to

Comparison operators return what is called a `boolean` value. Booleans can be true or false, and in Python are represented by the values `True` and `False`. Here are comparison operators in action:

	a = 1
	b = 2
	
	print a > b
	
	>>> False
	
	print b == a
	
	>>> False
	
	print 1 != 3
	
	>>> True
	
Generally, when we are comparing values, we want them to be the same type. For example, we will usually compare integers with other integers, strings with strings, etc. We can, however, compare two values of different types:

	a = 1
	b = 'hello'
	
	print a > b
	
	>>> False
	
	print b > a
	
	>>> True
	
Seems weird that this works, right? Also, why does Python decide that a string 'hello' is "greater than" 1? This was actually a mistake in [Python 2](https://docs.python.org/2/reference/expressions.html#not-in), which has been fixed in Python 3. These comparisons will return consistent, but irrelevant results.

###Conditional Statements

**If**

`if` statements let us test to see if an expression evaluates to `True`. Here is what they look like:
	
			if (2 > 1):
				print "2 is greater than 1"
				
			>>> 2 is greater than 1
			
`if` statements are pretty straightforward. The above can be abstracted to look like:

	if (this statement is true):
		#do this

Let's put `if` statements to work by making a procedure called `bigger`, which will return the greater of two values.

	def bigger(a, b):
		if(a > b):
			return a
		return b

	print bigger(2,7)
	>>> 7
	
Notice the two return values? That's okay, because only one will ever be reached anyway. If `a > b` returns `True`, our procedure will stop executing after `return a`, since the return statement is always the last piece of code executed in a procedure. If a is not greater than b, we won't run the code inside the `if` statement and instead skip to `return b`.

**Else**

Let's say we didn't like having two return values. Instead, we could re-write `bigger` to use an `else` statement in addition to the `if`:

	def bigger(a, b):
		if (a > b):
			big = a
		else:
			big = b
	
	return big
	
This is perhaps more readable, but does the same thing; in a lot of cases `else` statements can be necessary.

**Else if, a.k.a elif**

Maybe there are more than two cases we want to handle with a comparison. This is where the `elif` statement can come in handy:

	def happiness(x):
		if (x >= 10):
			return "I'm super happy!"
		elif (x >= 5):
			return "I'm kinda happy."
		else:
			return "Today sucks..."
			
	print happiness(13)
	
	>>> I'm super happy!
	
Pretty simple, right? We can have as many `elif` statements as we want.

**Or**

Let's say we wanted to make a procedure, called `vowel`, that will return `True` if the input is a vowel. Using `if` statements, it would look like this:

	def vowel(letter):
		if letter == 'a':
			return True
		elif letter == 'e':
			return True
		elif letter == 'i':
			
	# etc etc...

A better way to do this would be to use the `or` operator:

	def vowel(x):
		if (x == 'a' or x == 'e' or x == 'i' or x == 'o' or x == 'u'):
			return True
		return False
		
	print vowel('a')
	
	>>> True
	
	print vowel('b')
	
	>>> False

Granted, there are better ways of checking to see if a letter is a vowel, but hopefully you can see how `or` works. Basically, we are saying "if any of these conditions are true, do this".

An interesting aspect of `or` is that it only evaluates what it needs to in Python. For example, this would print `True`:

	print True or this_is_an_error
	
	>>> True
	
Even though the second statement, `this_is_an_error`, would indeed throw an error if evaluated on its own, since the `or` operator found a condition that was true, it never even needed to look at `this_is_an_error`.

**And**

`and` works in a similar way to `or`; it can be used to chain conditions together. With `and`, we are saying "if ALL of these conditions are true, do this":

	def medium(x):
		if (x > 3 and x < 10):
			return True
		return False
		
	print medium(1)
	
	>>> False
		
`medium(1)` returned `False` because it only met one of the conditions we specified.

###Let's Stop for a Second...

At this point, even if you were to not learn anything else, you could theoretically write any possible computer program. Pretty amazing, right? Anything that can be computed by a machine could be done using only what we know so far: arithmetic, simple procedures, and comparisons. 

This fact was first brought to life by [Alan Turing](http://www.bbc.co.uk/history/people/alan_turing) in the 1930s.Turing developed an abstract model of a computer, called a "Turing Machine", and proved that a machine with a few simple operations could simulate another machine.

Fun fact: a "computer" used to be a profession; computers were people who computed things.

Turing's discoveries and inventions were [instrumental in breaking Nazi encryption methods](http://en.wikipedia.org/wiki/Bombe) during WWII. A key difference between his computers and computers today is that back then, computers were not programmed. They were built for one purpose, just like a toaster.