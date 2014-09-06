# Web Development

**Udacity: CS 253**

## Lesson 6: Caching

#####Scaling a Website

Reasons to scale:

1. Handle more requests concurrently
2. Store more data
3. More failure resistance
4. Serve requests faster

What do we scale?

1. Bandwidth
2. Computers (RAM, CPU)
3. Power
4. Storage

For example, Google has the entire internet essentially indexed so it can perform fast searches. Facebook has millions of photos it must store.

Techniques for scaling:

1. Optimize Code

	* However, consider cost per machine vs cost per developer. Sometimes, adding more computational power can be better than paying better developers, since developers cost a lot of money.
	
2. Cache complex operations
3. Upgrade hardware

	* More machines
	* Faster CPU
	* More disk space
	
4. Add more hardware

#####Caching

**Caching**: storing the results of an operation so that future requests will be faster.

When to cache:

* When the output of a computation is the same every time for a given input
* When a hosting provider charges for database access
* When computation is slow

How does it work? Consider this function `db-read()`, which takes 100ms to complete. This means we can only do this 10 times per second. To cache this, we would have something like this:

	if request in cache: #cache is a dictionary or hash table
		return cache[request]
	else:
		r = db-read()
		cache[request] = r
		return r
		
The "if" statement is called a *cache hit* and the "else" statement is called a *cache miss*. Here is another example in Python:

	import time

	# complex_computation() simulates a slow function. time.sleep(n) causes the
	# program to pause for n seconds. In real life, this might be a call to a
	# database, or a request to another web service.
	def complex_computation(a, b):
    	time.sleep(.5)
    	return a + b

	cache = {}
	def cached_computation(a, b):
		key = (a,b)
    	if key in cache:
        	r = cache[key]
    	else:
        	r = complex_computation(a,b)
        	cache[key] = r
        return r

	start_time = time.time()
	print cached_computation(5, 3)
	print "the first computation took %f seconds" % (time.time() - start_time)

	start_time2 = time.time()
	print cached_computation(5, 3)
	print "the second computation took %f seconds" % (time.time() - start_time2)

The second computation will be immensely faster than the first, thanks to caching.

#####Optimizing Database Queries

* Optimize Code: limit the work the database has to do by having simple queries and indexing.

* More / bigger machines (if this is an option)

* Cache the database

	* Problems to consider:
	
		1. If more content is submitted to your site, clear or update the cache so that the new data shows up when the page is rendered, rather than just the old data that was already cached.
		
		2. Many users, one of which posts to the database, clearing the cache. Since all of the other requests are happening at the same time, the database gets "beat up" in what is called a **cache stampede**. The solution is to *overwrite the cache with new data* rather than clear it.
		
An important property that a website should have is that normal users never touch the database, only the cache. Users that post should be the only ones that query the database.

#####Updating the Cache

Write to the database and simultaneously update the cache as well, rather than reading from the database. This is faster but more complicated than refreshing the cache by reading from the database.

#####Load Balancing

Add multiple machines to handle simultaneous requests. Use a machine called a **load balancer** that keeps track of which servers have the most and least amount of load. It chooses a server to send a user's request to based on an availability score. 

Something like Google App Engine handles this for you.

Algorithms for load balancing:

1. Random: randomly choose a server to send requests to.
2. "Round Robin": Chooses one server at a time, in a specific order. In some cases, this algorithm will also consider load on each server and skip servers if needed.

#####Caching w/ Multiple Servers

Having a cache implemented as a hash table when there is only one server is fine, but what happens when this approach is tried with multiple servers?

* Multiple app servers = multiple caches. Impossible to keep in sync.
* Each app server may have to hit the database to update its cache.