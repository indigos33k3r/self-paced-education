#Intro to Computer Science

**Udacity: CS 101**

---

###Time to Finish the Web Crawler!

Right now, what we can do is grab all of the links from any given web page. What we need to do next is change the way we handle those links. Instead of printing them out and calling it a day, let's define a procedure called `get_all_links`, which will store all of those links in a list. Here it is:

	def get_all_links(page):
		links = []
		while (get_next_target(page) != None):
			url, marker = get_next_target(page)
			links.append(url)
			page = page[marker:]
		return links
		
It's not too big of a change from `print_all_links` that we had before. All we do differently is append each new link to a list, and then return that list at the end.

It's now time to finish the web crawler portion of our search engine! Now that we can get all of the links on a web page, we need to start following those links, while also keeping track of which links we have and haven't crawled yet, and then repeating the process on each new page we crawl.

Let's try working through this with pseudo-code:

	start with to_crawl = [seed]
	crawled = []
	while there are more pages in to_crawl:
		pick a page from to_crawl
		add that page to crawled
		add all of the links on this page to to_crawl
	return crawled
	
Oops! This will never return though, because we didn't consider a very important case: *circular links*. If two webpages that we are crawling link back to each other, we will always have links in `to_crawl	` and our procedure will go on forever. Here's a version that improves by checking to make sure we haven't already crawled a site:

	start with to_crawl = [seed]
	crawled = []
	while there are more pages in to_crawl:
		pick a page from to_crawl that is NOT in crawled
		add that page to crawled
		add all of the links on this page to to_crawl
	return crawled
	
We are now ready to write the code to make a procedure called `crawl_web`, which will take in a seed page as input, and output a list of all the URLs that can be reached by starting at that seed page. Here it is (with a helper procedure called "union"):

	def union(a, b):
		[a.append(x) for x in b if x not in a]

	def crawl_web(seed):
		to_crawl = [seed]
		crawled = []
		while to_crawl: # empty lists are interpreted as False, so this works
			page = to_crawl.pop()
			if page not in crawled:
				union(to_crawl, get_all_links(page))
				crawled.append(page)
		return crawled
		
We've now written a basic web crawler! Time to move on to learning how to make a search engine! Granted, this web crawler has some flaws (imagine trying to run it on something like Facebook; it'd run forever because there are too many links...), but hopefully you learned a lot about computer science and Python in the process of building it.