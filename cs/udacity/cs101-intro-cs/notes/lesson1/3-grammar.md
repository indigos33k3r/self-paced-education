#Intro to Computer Science

**Udacity: CS 101**

---

###Why Programming Languages Exist

Many people wonder why we have programming languages when widely used languages like English and Japanese already exist. There are two main reasons:

1. Natural languages are too ambiguous.
    * Computer must be able to interpret a program *exactly* as the programmer intended.
    * Example of ambiguity in natural language:
		* Would you rather be paid $100 weekly or bi-weekly?
			* This could be interpreted to mean:
				* $100/wk vs. $200/wk
				* $100/wk vs. $100 every 2 weeks
			* Ambiguity in computer programs would be a **terrible** thing; imagine if your bank's software didn't always interpret things the same way every time...
2. Natural languages are very verbose.
	* To write a program, we need to be accurate and precise. If we used natural languages to build software, a huge amount of text would be required to provide the necessary amount of precision that a computer needs.
	
###Grammar

Every programming language has a *grammar*, just like any natural language. A language's grammar is very important; it prevents ambiguity and defines what is part of that language. For example:

	# legal Python code
	print 2 + 2
	
	# illegal Python code (will throw an Error)
	print 2 + 2 +
	
###Backus-Naur Form

Backus-Naur is a grammar invented in the 1950s by [John Backus](http://www.thocp.net/biographies/backus_john.htm), the inventor of the Fortran programming language.

Its purpose is to precisely and simply describe a language's notation. It works like this:

	<non-terminal> -> replacement

Essentially, you start with a non-terminal, and keep replacing it until you get to a terminal. Here's an example, using sentence structure. A terminal will be indicated with an asterisk.

	Sentence -> Subject Verb Object
	Subject -> Noun
	Object -> Noun
	Verb -> Eat*
	Verb -> Like*
	Noun -> I*
	Noun -> Python*
	Noun -> Cookies*

Using BNF, we have defined a limited but structured grammar. Let's *derive* a statement from this:

	Sentence -->
	Subject Verb Object -->
	Noun Verb Noun -->
	I like Python.

Using the given data (which can be infinitely large) and the small rules of replacement grammars, we were able to derive a real sentence. Let's see grammar put to use in Python:

###Python Grammar for Arithmetic

Python's grammar works like this:

	Expression -> Expression Operator Expression

This is a [recursive](http://en.wikipedia.org/wiki/Recursion) definition (note that an Expression can be replaced with another Expression), so we need two rules: one for where we can keep going, and one for where we stop (so we don't have [infinite recursion](http://www.nature.com/scitable/content/ne0000/ne0000/ne0000/ne0000/20688073/2_1.jpg)).

	Expression -> Expression Operator Expression
	Expression -> Number
	Expression -> (Expression)
	Operator -> +
	Operator -> *
	Number -> 0,1,2,3...
	
There are more operators and numbers in Python, but this limited set will work for now.

Following these rules, we can derive:

	Expression -->
	Expression Operator Expression -->
	Number + (Expression) -->
	Number + (Expression Operator Expression) -->
	2 + (Number Operator Number) -->
	2 + (2 * 3)
	
Notice how Expression was replaced with (Expression Operator Expression) in the above example.



