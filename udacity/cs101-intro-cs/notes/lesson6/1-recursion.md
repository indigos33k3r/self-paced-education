#Intro to Computer Science

**Udacity: CS 101**

---

###Lesson 6: Recursion

We will use something called *recursion* to help make the final improvements to our search engine. Let's explain recursion by starting with a question: what is the largest word in the English language?

Well, there isn't one. You can give me a 100-character word, but I can always make it longer. Remember how BNF grammar told us that expressions can be made from other expressions? That's a recursive definition. The same applies to words:

	Word: intelligence
	New word: counterintellignce
	New new word: counter-counterintelligence
	etc...
	
We could go on forever, just adding the same prefix to a word. The point is, because English has a rule that lets us make new words from old words, there is no "longest word". If this was the *only* rule English had, how many words could we make?

	Rule: Word --> counter-Word
	
The answer is none, because there are no *terminals*, only infinite replacements. This is a circular definition. What makes recursion work is that there is always a *base case*, where things terminate. This is a new set of rules that work:

	Word --> counter-Word
	Word --> hippo
	
We could make infinitely many words using those rules! Here's how all recursive definitions work:

1. Recursive case: we can define something in terms of itself
2. Base case: a case where the recursion stops or terminates

###Recursive Definitions

Now that we know how recursion works conceptually, let's apply it to programming. As we said before, recursive definitions involve two cases:

1. Base case
	* Starting point
	* Not defined in terms of itself
	* Based on the smallest possible input, where we already know the answer
2. Recursive case
	* Defined in terms of itself
	* Goal is to work towards the base case
	
Before we start writing code, let's try to use recursion to solve the problem of trying to find our ancestors. The way to think about ancestors is with a family tree:

								You
								/ \
							   /    \
						   Parent   Parent
						  /            \
						 /              \
					Grandparent	    Grandparent
	
As you can see, your parents aren't the only ancestors that you have. We could keep going, including great-grandparents, etc. Our goal is to figure out a recursive definition for ancestors. Here's one that works:

	Ancestor --> Parent
	Ancestor --> Parent of Ancestor
	
This gives us the room to have an infinite amount of ancestors, but is still not a circular definition. This definition works because it has the two rules we need (base case and recursive definition).

###Procedures

**Factorial**

It's now time to learn how to define procedures using recursion. You may recall the `factorial` function from Lesson 2: it's the number of ways we can order `n` items. It can be expressed like this:

	factorial(n) = n * (n-1) * (n-2) * ... * 1
	
Unfortunately, humans understand what that means (the "..."), but computers don't. This is where a recursive definition can come in handy. We know that the factorial of 0 is 1, so let's have that be our base case. For every other number `n`, the factorial is `n * factorial(n-1)`. That's our recursive case. Here's how that looks in code:

	def factorial(n):
		return 1 if n == 0 else n * factorial(n-1)
		
It might seem weird that we are calling a procedure from within itself, but that's exactly how recursion works! Here's a way to visualize how the computer processes recursion on the stack:

![recursion](../img/recursion.png)

Seems like a lot of work, right? Actually, it is. Although recursion can make your code more readable, and is sometimes necessary, it is certainly not a fast process. In a lot of cases, the recursive definition may be worse than the iterative or non-recursive definition (although, a lot of compilers will turn [tail recursive](http://stackoverflow.com/questions/33923/what-is-tail-recursion) code into iterative machine code anyway).

**Palindromes**

A palindrome is a string that reads the same forwards in backwards. Examples of palindromes include:

1. "a"
2. "pop"
3. "level"
4. ""
5. etc...

Could we perhaps define a recursive procedure that tests whether or not a string is a palindrome? (Yes, there are ways to do it without recursion)

	def is_palindrome(s):
    		if len(s) < 2:
         	return True
     	elif s[0] != s[len(s)-1]:
         	return False
     	else:
         	return is_palindrome(s[1:-1])
		
Our code works by first checking if the string is 0 or 1 characters in length. If so, it's a palindrome! If not, we check to make sure that the first letter matches the last letter. If it does, we chop those two letters off and keep going until we get to either one letter, or a case of the first and last letters not matching. For fun, here's a non-recursive way to do this in Python:

	def is_palindrome(s):
		return s == s[::-1]
		
This is a lot easier, but remember that we can't do it that simply in every language out there!

###Recursion vs. Iteration

As was mentioned before, any recursive procedure can be written in a non-recursive way. Sometimes, iteration is a better way to go about things. Let's prove that with some clock times on two procedures that calculate [Fibonacci numbers](http://en.wikipedia.org/wiki/Fibonacci_number). 

The Fibonacci number of `n` is defined as the the Fibonacci number of `n-1` and `n-2`, where the base *cases* are that the Fibonacci numbers of 0 and 1 are 0 and 1, respectively.

One difference here is that we will have two base cases for the recursive procedure!
	
	import time
	
	def watch(func):
		start = time.clock()
		eval(func)
		runtime = time.clock() - start
		return runtime
		
	def recursive_fib(n):
		return n if n < 2 else recursive_fib(n-1) + recursive_fib(n-2)
		
	def iterative_fib(n):
    		a, b = 0, 1
    		for i in range(0, n):
        		a, b = a + b, a #note use of multiple assignment
    		return a
    	
    	print "Iterative:"
    	print watch('iterative_fib(0)')
    	print watch('iterative_fib(10)')
    	print watch('iterative_fib(20)')
    	print watch('iterative_fib(30)')
    	print watch('iterative_fib(40)')
    		
    	print "Recursive:"
    	print watch('recursive_fib(0)')
    	print watch('recursive_fib(10)')
    	print watch('recursive_fib(20)')
    	print watch('recursive_fib(30)')
    	print watch('recursive_fib(40)')
		
And here are the runtimes (in seconds) for each procedure. Watch with horror has the recursive definition fails quickly:

	N			Recursive			Iterative
	--------------------------------------------
	0			3.6 x 10^-5			5.6 x 10^-5
	
	10			6.6 x 10^-5			3.3 x 10^-5
	
	20			0.00294606			2.9 x 10^-5
	
	30			0.3628				2.39 x 10^-5
	
	40			46.029				2.6 x 10^-5

The problem with the recursive definition is that as `n` grows, the number of calls grows at an explosive rate. When evaluating `fib(36)`, for example, we have to evaluate `fib(30)` a staggering 13 times! That's why we run out of memory as the input grows. Fibonacci numbers re a great example of when to not use recursion. Here's a cool visualization of the inefficiency of the recursive Fibonacci procedure: [Online Python Tutor](http://pythontutor.com/visualize.html#code=def+fib(n\)%3A%0A++++return+n+if+n+%3C+2+else+fib(n-1\)+%2B+fib(n-2\)%0A++++%0Afib(5\)&mode=display&origin=opt-frontend.js&cumulative=false&heapPrimitives=false&drawParentPointers=false&textReferences=false&showOnlyOutputs=false&py=2&rawInputLstJSON=%5B%5D&curInstr=0). Notice how the iterative version stayed at a power of 10^-5 regardless of the input size. It's much more efficient!