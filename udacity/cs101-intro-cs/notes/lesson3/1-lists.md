#Intro to Computer Science

**Udacity: CS 101**

---

###Lesson 3: Managing Data

**Lists**

At this point we know that a `string` is a sequence of characters. It's now time to introduce a way to have a sequence of *anything*: the list.

In a list, the elements can be:

* Strings
* Numbers
* Other lists (called "nested lists")
* Characters
* A combination of any of the above
* Your own data structures
* etc...

Here's an example of a list: `my_list = ['a', 'b', 'c']`. Lists, just like strings, are indexed. So, to get the first element in the list, we can do this: `my_list[0]`.

Look below to see more of what you can do with lists:

	#lists
	
	my_list = ['a', 'b', 'c', 'Hello', 12, 0, 2.2, ['another list in the list', 'yay']]
	
	print my_list[0]
	
	>>> 'a'
	
	print my_list[2:4]
	
	>>> ['c', 'Hello']
	
	print my_list[-1]
	
	>>> ['another list in the list', 'yay']
	
	for item in my_list:
		print item * 2
		
	>>> aa
	>>> bb
	>>> cc
	>>> HelloHello
	>>> 24
	>>> 0
	>>> 4.4
	>>> ['another list in the list', 'yay', 'another list in the list', 'yay']
	
	#"list comprehensions": more advanced, but you'll see more of this later
	
	nums = [0,1,2,3,4,5]
	squared = [x**2 for x in nums]
	
	print squared
	
	>>> [0, 1, 4, 9, 16, 25]
	
	print nums[::-1]
	
	>>> [5, 4, 3, 2, 1, 0]
	
Hopefully, you can see why being able to put things into a list can be helpful. It is a good way to store data, so that we can operate on that data whenever we want to. Let's look at a more structured example (note how I can type out the list on more than one line for organization):

	# the beatles
	
	beatles = [
		['John', 1940],
		['Paul' 1942],
		['Ringo' 1940],
		['George', 1943]
	]
	
	print beatles[3]
	
	>>> ['George', 1943]

	# accessing the indices of the nested lists

	print beatles[3][1] + 1
	
	>>> 1944
	
###Mutation

The second difference between strings and lists is that lists support something called *mutation*. Mutation means that we can change the value of a list after we've created it.

Recall what happens with strings:

	s = 'string'
	s = 'hello'
	
	# we changed the value of s, but NOT the string itself.
	# if we try to do that, we will get an error:
	
	s[0] = 'j'
	
	>>> TypeError: 'str' object does not support item assignment
	
Here's what happens with lists:

	p = ['H', 'e', 'l', 'l', 'o']
	
	# we could just assign p to a new list, but instead, we can change the list itself:
	
	p[0] = 'J'
	
	# the value of the original list is now:
	
	print p
	
	>>> ['J', 'e', 'l', 'l', 'o']
	
	q = p
	
	q[4] = 'hahaha'
	
	print q
	
	>>> ['J', 'e', 'l', 'l', 'hahaha']
	
	# THIS ALSO CHANGES THE VALUE OF p[4]
	
	print p
	
	>>> ['J', 'e', 'l', 'l', 'hahaha']
	
Now you know the difference between mutable and non-mutable objects! The way that mutable objects behave can be described by something called *aliasing*. Aliasing is when two objects, like `p` and `q` in our previous example, refer to the same object and are therefore indistinguishable. Here's a more complex example:

	james_bond = [0,0,7]
	spy = james_bond

	james_bond[2] = spy[2] + 1
	
	print spy
	
	>>> [0,0,8]
	
###List Operations

Just like we have `find()` for strings, we have plenty of operations we can perform on lists. Here are some important ones:

1. `append`
	* Append is used to add an element to the end of a list.
	
			stooges = ['Moe', 'Larry', 'Curly']
			
			stooges.append('Shemp')
			
			print stooges
			
			>>> ['Moe', 'Larry', 'Curly', 'Shemp']
2. List addition
	* This works just like concatenation for strings
	
			nums = [0,1]
			more_nums = [2,3]
			
			print nums + more_nums
			
			>>> [0,1,2,3]
3. `len`
	* `len` gets the number of elements in a list (or string)
	
			nums = [0,1,2,3]
			
			print len(nums)
			
			>>> 4
			
			print len("hello")
			
			>>> 5
			
			nested = [[0, 1], 2, 3]
			
			print len(nested)
			
			>>> 3

Let's see all of these operations used together:

	p = [1, 2]
	p.append(3)
	p = p + [4, 5]
	
	print len(p)
	
	>>> 5