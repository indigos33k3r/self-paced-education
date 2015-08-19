#Intro to Computer Science

**Udacity: CS 101**

---

###Lesson 5: How Programs Run

**Cost**

How much does it cost, in terms of time and resources, to run a program? The study of this is called *algorithm analysis*. Recall our definition of a procedure:

A procedure is a well-defined sequence of steps that can be executed mechanically. It must be guaranteed to finish and produce the correct result.

How computers think about cost is not in terms of money, but in terms of two things:

1. Time: How long does it take for the program to finish? (still very important)
2. Memory: How much memory does the computer use? (less important these days)

As the size of the input to a program grows, how does the amount of time and memory that program takes increase? This question matters because inputs change, and we want to be able to understand properties of our algorithms, not just how well it performs in one case or on one machine. Ideally, we'd also like to predict how long it will take for our program to run,  and know how the runtime will change as [computers get faster and faster](http://en.wikipedia.org/wiki/Moore's_law).

**Runtime**

For more on why scalability for our algorithms is important, let's start timing our code. Notice the `import time` statement at the top? What that is saying is that we are going to use some code packaged into an external *module*. It's code we could write ourselves, but someone else did it for us. `time` is going to let us run a stopwatch on our code:

	import time
	
	def watch(code):
		start = time.clock()
		result = eval(code) # eval lets us run any Python expression or procedure
		run_time = time.clock() - start
		return result, run_time

	def spin(n):
		i = 0
		while i < n:
			i += 1
			
Try running `watch` in your Python shell. Here's some example inputs and outputs:

	`watch('1 + 1')`
	
	>>> 2, 3.19999999999999e-05
	
That's a simple and fast calculation, so it's not very useful on it's own. Clearly, adding 1 and 1 won't take much time. What about our `spin` procedure, with growing inputs?

	In [7]: watch('spin(100)')
	Out[7]: (None, 8.20000000000265e-05)

	In [8]: watch('spin(1000)')
	Out[8]: (None, 0.00013799999999997148)

	In [9]: watch('spin(10000)')
	Out[9]: (None, 0.0017250000000000876)

	In [10]: watch('spin(100000)')
	Out[10]: (None, 0.008573000000000053)

	In [11]: watch('spin(1000000)')
	Out[11]: (None, 0.07743499999999992)

	In [12]: watch('spin(10000000)')
	Out[12]: (None, 0.57558)

	In [13]: watch('spin(100000000)')
	Out[13]: (None, 5.6246469999999995)

	In [14]: watch('spin(1000000000)')
	Out[14]: (None, 60.063536)

As you can see, as the input grew by powers of 10, the time increased by a gigantic amount. We went from around 5 seconds to a minute when the input grew from 10^8 to 10^9.

You may notice that as the input grew by factors of 10, the time grew by around the same amount. We would call the runtime *linear* in this case; it grows at the same rate as the input, no matter what.

**Worst case**

What we generally care about when analyzing execution time is the worst case. Let's say we have our `lookup` procedure from the search engine:

	def lookup(index, keyword):
		for entry in index:
			if entry[0] == keyword:
				return entry[1]
		return None
		
What keywords would result in a worst-case runtime for `lookup`? The answers are either a word that is not in the index, or the very last word in the index. This is because we will have to go through the entire `for` loop for those inputs.

**Constant time operations**

You may be wondering why we only cared about the `while` loop when looking at the runtime of `spin` from a little while ago. Doesn't the stuff inside the loop (in this case, `i += 1`) take time too?

The answer to that is yes, assigning that new value to `i` does take time. However, since that code does not depend on the size of the input at all, we call it a **constant time operation**. That means that no matter what, `i += 1` will always take the same amount of time. We only want to analyze portions of our code whose execution times vary with the input.

**Improving efficiency**

We now know an unfortunate truth about `lookup`: it will take a really long time if we have a large index. How can we change that? There are several ways:

1. Sort our index: make it easier to find different parts of the index without iterating over the entire thing every time
2. Hashing: A *hash* function will let us map each keyword to a specific place in the index, making for instant lookups. This is what we will do.

**Hashing**

A simple *hash function* would create lists within the index based on starting letter. All of the words that start with 'u' would be in one place. We'll call this list within the index the *bucket* of words that start with 'u'. 

This isn't quite the best way to do things, because of scaling problems: at best, our hashing function will only make things around 26 times better. When we go from 10,000,000 to 1,000,000,000 words, that advantage doesn't seem so good. Additionally, that 26 number assumes that every starting letter is equally popular; we know this not to be true. That means that we end up with two problems:

1. Words with popular starting letters, like 's' and 't',  will be stored in a very large list, which will be slow to iterate through
2. People are going to look up these types of words more, so our fancy new hash function didn't really solve anything.

So, looks like our initial idea doesn't work. What other types of hash functions could we use to break up our index?

Suppose we have `b` buckets and `k` keywords, and there are more keywords than buckets. Our hash function should have these properties:

1. It should output a number between 0 and `b` - 1 when generating indices for keywords
2. It should map approximately `k/b` keywords to every bucket

More on our hash function in the next set of notes!