#Intro to Computer Science

**Udacity: CS 101**

---

###Hashing

**Defining our hash function**

We want our hash function, called `hash_string`, to take in a string, and output a number between 0 and `b-1`. We can use two new operators to help us do this:

* `ord`, which takes a character and returns its [ASCII value](http://www.asciitable.com/)
* `chr`, which does the reverse

Let's see them in action:

	print ord('a')
	
	>>> 97
	
	print chr(97)
	
	>>> a
	
Since we want our hash function to output a value in a specific range, we can also use something called the `modulus` operator, which is represented by the `%` character.

Modular arithmetic works somewhat like a clock; if we have a clock with 12 hours on its face, we can't have any values greater than 12. So we use the modulo operator to get remainders when dividing by that max value (12 in this case). 14 % 12 = 2, 12 % 12 = 0, 1 % 12 = 1, etc. More on modular arithmetic can be found [here](http://www.math.rutgers.edu/~erowland/modulararithmetic.html).

Let's write our first hash function, now that we know enough:

	def crappy_hash(keyword, buckets):
		return ord(keyword[0]) % buckets
		
There are many problems with this hash function, but it's a start:

1. It produces an error for an empty string, which is a valid input
2. If the keywords are distributed like words in English, some buckets will get very large
3. If the number of buckets is large, some buckets will get no keywords put in them

**Making a better hash function**

We need to improve the way we distribute our keywords into buckets. Therefore, we can't just look at the first letter in each word. Recall that we can use a loop to iterate over all of the characters in a string:

	for c in string:
		print c
		
Here's a better hash function: it works by adding up the ordinal value of each character in the string, and then getting the remainder of that total when divided by the number of buckets.

	def hash_string(keyword, buckets):
    		total = 0
    		for char in keyword:
        		total += ord(char)
    		return total % buckets

	print hash_string('udacity', 12)
	
	>>> 11
	
	print hash_string('a', 13)
	
	>>> 6
	
	print hash_string('', 10)
	
	>>> 0
	
This solution is still far from perfect, but at least it handles that empty string better, and wouldn't result in lots of empty buckets. We can test out our hash function by creating a procedure to test the distribution of words in the buckets:

	def test_hash(fund, keys, size): #note that we can pass a function as a parameter
		results = [0] * size
		keys_used = []
		for w in keys:
			if w not in keys_used:
				hv = func(w, size)
				results[hv] += 1
				keys_used.append(w)
		return results
		
Running that against our hash function, with [this](http://www.gutenberg.org/cache/epub/1661/pg1661.txt) input string (called `words`) produces this distribution when we have 12 buckets:

	 print test_hash(hash_string, words, 12)
	 
	 >>> [1363, 1235, 1252, 1257, 1285, 1256, 1219, 1252, 1290, 1241, 1217, 1303]
	 
While the distribution into the buckets is not perfectly even, it's not terrible.

One problem with our hash function, recalling our lesson on runtime, is that the `for` loop makes it take very long for large inputs. For now though, we've covered enough about hash functions. There are very good ones out there, and I'd encourage you to do research into designing the best hash functions. One to take a look at is the popular [Fowler-Noll-Vo hash](http://en.wikipedia.org/wiki/Fowler%E2%80%93Noll%E2%80%93Vo_hash_function).

###Hash Tables

Our previous data structure for the index was a bunch of nested lists:

	index = [
		[keyword, [url, url, url]],
		[keyword, [url, url, url, url]],
		etc...
	]
	
To make our data structure better for hashing, let's change it around a bit to represent buckets:

	index = [
		[
			[word, [url, url, url]],
			[word, [url, url]]	
		],
		[
			[word, [url, url, url, url]]	
		]
	]
	
As you can see, our structure is getting pretty complex. Each element of the index is a list, which represents one bucket. Inside each bucket is another list, containing the keywords and lists of URLs. Ouch...

**Creating an empty hash table**

Before, our index could be initialized like this: `index = []`. Now that it's a hash table, it needs to start with all of the buckets in place, since we want to be able to do lookups right away.

We can do this to create our table now:

	def make_hashtable(nbuckets):
    		return [[] for i in range(nbuckets)]
		
Pretty simple, right? It will create a list containing the correct number of empty lists, a.k.a. buckets.

NOTE: You may be tempted to write this: `return [[]] * nbuckets`, but the problem with that is that `*` creates multiple references to the same list, rather than 3 copies of the list. That means appending anything to any of the sub-lists will also append it to the other sub-lists.

**Finding Buckets**

We need to now define a procedure, which we will call `get_bucket`, that takes two inputs: a hash table and a keyword, and outputs the bucket where the keyword could occur:

	def get_bucket(table, keyword):
    		return table[hash_string(keyword, len(table))]

	def hash_string(keyword, buckets):
    		out = 0
    		for s in keyword:
        		out = (out + ord(s)) % buckets
    		return out
	
	def make_hashtable(buckets):
    		table = []
    		for i in range(0, buckets):
        		table.append([])
    		return table
		
**Adding keywords**

Let's make a procedure, called `hashtable_add`, that will add a key to the table in the correct bucket, and return the new table:

	def hashtable_add(table, key, value):
		b = get_bucket(table, key)
		b.append([key, value])
		return table

Notice a problem? This procedure will insert duplicates into the bucket, so we need to fix that. First, let's define a `lookup` procedure that takes two inputs, a hash table and a key, and outputs the value associated with that key (or `None` if it isn't there):

	def lookup(table, key):
    		bucket = get_bucket(table, key)
    		for e in bucket:
        		if e[0] == key:
            		return e[1]

The last change we need to make is making `hashtable_add` update the table rather than insert a duplicate key when two of the same keys are inserted:

	def update(table, key, value):
    		bucket = get_bucket(table, key)
    		for entry in bucket:
        		if entry[0] == key:
            		entry[1] = value
            		return table
    		bucket.append([key, value])
    		return table

We're pretty much done with our hash table at this point! Now, as the number of keys increase, as long as we increase the number of buckets, lookup and add both take constant time.