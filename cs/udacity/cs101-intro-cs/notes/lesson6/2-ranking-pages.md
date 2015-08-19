#Intro to Computer Science

**Udacity: CS 101**

---

###Ranking Webpages

Now that we know everything we need to in terms of concepts, it's time to learn how to let our search engine rank webpages. Ranking websites is incredibly important in this day in age, as there is so much content on the internet. 

This is how Google was able to distinguish itself from other search engines; their "PageRank" (named after CEO Larry Page) algorithm is described [here](http://en.wikipedia.org/wiki/PageRank#Algorithm).

**Defining Popularity**

Right now, our search engine returns URLs for a given keyword search in the order that they were put into the index. This would be okay if the internet was very small, but it isn't.

First, we need to cover this in a conceptual way: how do we decide who is popular in high school? One way is to go by the number of friends someone has. For our purposes, we will assume that friendship is one-directional. This means that if I am friends with you, you don't necessarily have to be friends with me. This is illustrated below:

![friends](../img/friends.png)

Unfortunately, just having a lot of friends isn't enough to be considered popular (at least if you went to most public high schools). You've got to have the *right friends*, a.k.a. friends who also have a lot of friends.

How can we define popularity in code? Here's an attempt:

	def popularity(p):
		score = 0
		for f in friends(p):
			score += popularity(f)
		return score
		
Hmm, looks like we tried to make a recursive definition without having a base case. This definition, in a lot of cases, would cause the procedure to run infinitely; it's a circular definition. We need a way of stopping, so let's try to define a pretend base case:

	def popularity(p):
		if p == 'Alice':
			return 1
		else:
			score = 0
			for f in friends(p):
				score += popularity(f)
			return score
			
This still doesn't work! What if nobody is friends with Alice? We'd end up in an infinite loop again. In fact, the only time this would work is if we had something that looked like this:

	Bob ---> Charlie --> Alice
	
###Relaxation

So, there appears to be no sensible base case for finding the popularity score of an individual. To continue onward, we need something called a *relaxation algorithm*. What this algorithm will do is:

1. Start with a guess
2. While we aren't done, make the guess better

Seems pretty vague, right? It works by refining our guess until we can't refine it anymore. Our procedure will now look like this:

	def popularity(step, person):
		# do stuff


That extra `step` parameter will be our base case. At step 0, everyone's popularity is 1. So, we can figure out the popularity of any person at step `t` as the sum of the popularity of all of their friends, with step `t-1`. That may not be clear at first, so let's look at it as Python code:

	def popularity(t, p):
		if t == 0:
			return 1
		else:
			score = 0
			for f in friends(p):
				score += popularity(t-1, f)
			return score
		
While this itself may not be the best way to define popularity, it is at least a starting point: a real recursive algorithm.

###Graphs

For our search engine, instead of thinking about friends, think about links. We want to get a measure of how popular a page is based on two things:

1. How many pages link to our page
2. The *quality* of those links: how many pages link to that pages that link to our page

To give popularity a numerical value, we can look it a random web surfer (someone just browsing the internet): 

The popularity of page `x` is the **probability that a web surfer will land on page `x`, given a starting page**. We can base this probability partly on the two things we talked about above, and partially on the amount of *outgoing* links a page has (we won't worry about that part for now). We can also consider the proposition that for pages with tons of links, the value of each of those links goes down (just like having a few good friends is better than a lot of decent ones). The last component will be something called a *damping* function, which will tell us the probability that a random web surfer will pick a random link, versus starting over again on a new random page. A typical value for this is `0.8`. It will help us see how likely it is that a random web surfer who starts over will start at page `x`.

We are going to define something similar to the popularity function to get us started. The step `t` will state that all URLs start with the same rank, just like before.

It's now time for us to implement our ranking algorithm:

We need to keep track of the link graph (what pages link to other pages). In computer science, a graph is just a set of nodes with links to other nodes. Since our links are one-way, we call this type of graph a *directed graph*.
	
We can use a dictionary to do this:

	graph = {
		url: [pages it links to],
		url2: [pages it links to]
	}
	
Our goal is to modify the crawl_web procedure from before that produces an index *and* a graph of outgoing links now. Here's the old code:

	def to_crawl(seed):
		to_crawl = [seed]
		crawled = []
		index = {}
		while to_crawl:
			page = to_crawl.pop()
			if page not in crawled:
				content = get_page(page)
				add_page_to_index(index, page, content)
				union(to_crawl, get_all_links(content))
				crawled.append(page)
		return index
		
We can change it like this to suit our new needs:

	def to_crawl(seed):
		to_crawl = [seed]
		crawled = []
		index = {}
		graph = {}
		while to_crawl:
			page = to_crawl.pop()
			if page not in crawled:
				content = get_page(page)
				add_page_to_index(index, page, content)
				outlinks = get_all_links(content)
				union(to_crawl, outlinks)
				graph[page] = outlinks #here's the magic line!
				crawled.append(page)
		return index, graph
		
That was pretty simple! Now that we have our graph, we can move on to the final step in building our search engine.

###Finishing the Search Engine

We're so close! Let's finish up by making a procedure, `compute_ranks`, that will take in the graph from `crawl_web` and output a dictionary containing URLs and their ranks. The higher the rank, the better. We will need to keep track of the current and previous rank, so we can fairly update page ranks. Lastly, we will add a `lookup_best` procedure to give us the highest ranked page when we input a keyword.

	def compute_ranks(graph):
		d = 0.8 # damping factor
		num_loops = 10 # arbitrary, but decent
		ranks = {}
		
		npages = len(graph) # nodes in the graph
		for page in graph:
			ranks[page] = 1.0 / npages
			
		for i in range(0, num_loops):
			new_ranks = {}
			for page in graph:
				newrank = (1 - d) / npages
				for node in graph:
					if page in graph[node]:
						newrank += d * (ranks[nodes] / len(graph[node]))
				newranks[page] = newrank
			ranks = new_ranks
		return ranks
		
We're all done!