#Intro to Computer Science

**Udacity: CS 101**

---

###Loops

**While loops**

`while` loops are used for doing things over and over again, as long as a condition is true. Here's an example:

	i = 0
	while (i < 10):
		print i
		i = i + 1
	
	print "we aren't in the loop anymore!"
	
The above code would print the value of `i` (initially set to 0), increment it by 1, and go back to the start of the loop until i was no longer less than 10. Its output would be:

	0
	1
	2
	3
	4
	5
	6
	7
	8
	9
	we aren't in the loop anymore
	
Loops will be a very important piece of our search engine! Be careful with them though, as *infinite loops* can be a problem. This code will run forever (well, until our PC runs out of memory at least):

	i = 0
	while (i < 10):
		print i
		
	print "this will never get printed because i will always be less than 10"
	
**For loops**

`for` loops work by iterating over something until they run out of "things" to iterate over. They are similar to `while` loops, except the iteration is taken care of for us. See this example:

	for i in range(0, 10):
		print i
	
The above code would print out the numbers 0 to 9, since the `range()` method's second argument is not inclusive (there's `xrange()` if you want to include both). We will focus on `for` loops later down the road a lot more, as they are very useful when *data structures* come into play. Stay tuned!

**Break**

`break` can be used to exit a loop abruptly, regardless of whether or not the test condition is true. Let's see it in action here:

	i = 0
	while (i < 10):
		print i
		i = i + 1
		if (i == 7):
			break

This code would make the `while` loop exit as soon as `i` hits 7, rather than continuing all the way to 10.