#Intro to Computer Science

**Udacity: CS 101**

---

###Lesson 4: Responding to Queries

At this point in the class, we have a working web crawler. The focus of this unit will be using that web crawler to build a search engine that can crawl and build an index of a set of pages, and then respond to keyword queries.

To accomplish this, we will need to learn about designing and using data structures. We will also learn more about the internet in general.

###Data Structures

The structure we will be need is called an *index*; the type of index we are talking about is just like the index in the back of a book. We want an index that provides a mapping of keywords to the pages that contain those keywords.

Our index could look something like this (using lists):

	index = [
		[keyword, [url, url, url]],
		[keyword2, [url]]
	]

Each list inside of `index` contains a keyword, followed by another list of all the URLs containing that keyword. There are certainly other ways to structure our index, but this one is nice because it separates the keywords from the URLs, and is extensible: we could also easily add in a list for the number of times a keyword was searched for without changing anything else.

Let's jump right into things by creating a procedure, called `add_to_index`, which will take  inputs: an existing index (with the structure we designed above), a keyword, and a URL.

`add_to_index` should do two things:

1. If the keyword is not in the index, add it to the index.
2. If the keyword is in the index, add the URL to the list of URLs associated with the keyword.

Here's one way to do it:

	def add_to_index(index,keyword,url):
		for e in index:
			if e[0] == keyword:
				return e[1].append(url)
		index.append([keyword, [url]])
    
Now that we can build an index, we need to use it! How can we respond to queries? Let's create a procedure called `lookup`. It will take two inputs, an index and a keyword. It's output should be the list of URLs associated with that keyword. Lookup is even simpler than adding to the index:

	def lookup(index,keyword):
    		for e in index:
        		if e[0] == keyword:
            		return e[1]
    		return []		

It will return an empty list in the case that the keyword was not found. Let's move on to building the web index. To do this, we need to learn about a method called `split()`. It works like this:

	message = "Today is a wonderful day!"
	words = message.split()
	
	print words
	
	>>> ["Today", "is", "a", "wonderful", "day!"]

You can also pass in a *delimiter* to `split`, which will tell the method to break up the string at that point rather than the default of spaces:

	message = "This,has,lots,of,commas"
	words = message.split(",")
	
	print words
	
	>>> ["This", "has", "lots", "of", "commas"]

We can now define another procedure, called `add_page_to_index`, that will take three inputs:

1. The current index
2. A URL
3. The page content of that URL

It needs to update the index to include all of the word occurrences found in the page by adding the URL to the word's associated URL list.

	def add_page_to_index(index, url, content):
		words = content.split()
		for word in words:
			add_to_index(index, word, url)
			
Granted, this isn't perfect: we will get a lot of content that isn't words, like HTML tags and Javascript code, etc. But it's good enough for our purposes! Let's finish up the web crawler now. We can do this with a one-line modification to our `crawl_web` procedure:

	def crawl_web(seed):
		to_crawl = [seed]
		crawled = []
		while to_crawl:
			page = to_crawl.pop()
			if page not in crawled:
				content = get_page(page)
				add_page_to_index(index, page, content)
				union(to_crawl, get_all_links(content))
				crawled.append(page)
		return crawled
		
We're done!