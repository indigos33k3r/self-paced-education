# Web Development

**Udacity: CS 253**

## Lesson 3: Databases

#####What is a database?

A program that stores and retrieves data, generally large amounts.

* Generally, there is a separate *database server*, serrate from the *web server* that we have been working with so far.

#####Tables

1. *Columns*: Categories in the table, such as name, value, date, ID, GPA, etc...

	* Here is an example of columns for a table of college students:
	
			ID	Name	Major	Class	Student ID	GPA
	
2. *Rows*: One instance of an element in a table. For example, in a table of college students, one student would make up a row.
	
	* Generally, each row in a database will have an **ID**. This is usually an integer, but Google App Engine allows strings as well.
	
#####Why databases?

Downsides of querying by hand, for one:

1. Error prone
2. Tedious
3. Slow (imagine having millions of rows to handle)


#####Types of databases

* Relational Databases

	* Ex/ Postgresql, MySQL (most popular), SQLite, Oracle
	* Generally use the SQL querying language to store and access information
	
* "NoSQL" Databases

	* Ex/ MongoDB, Couch
	* Generally use JSON to store data objects
	
* Others

	* Google App Engine Datastore, Amazon Dynamo, etc.

#####SQL: Structured Query Language

Used in relational databases to post and get data, invented in the 1970s, before the internet.

* Example: ```SELECT * FROM links WHERE id=5```

	* SQL is great because of its readability. The query is self-explanatory: get all of the rows from the "links" table that have the id "5" (this is the 'constraint')
	
* More advanced queryL ```SELECT * FROM links WHERE id=5 OR title="Hello"```

#####More SQL

**The ```ORDER BY``` clause:**

* ```SELECT * FROM links WHERE id=5 ORDER BY votes DESC``` (ascending is default)

**Joins**

* Involve working with multiple tables; result in less unnecessary queries:

	Table 1 (Link): 
	
		ID	Votes	User-ID		Date	Title	URL
	
		5	206		22			1/22/13	blah	example.com
		
	Table 2 (User):
	
		ID	Name	Password	Date
		
		22	spaz	huehuehue	1/22/13
		
	* An example query for these tables would be: ```SELECT link.* FROM link, user WHERE link.user_id = user.id AND user.name = spaz```
	
	* Joins, while useful in some applications, aren't very useful for web apps overall.
	
#####Indexing

* Make lookups faster with indexes

	1. Hash Table: mapping of a key to a value, provides constant-time lookup. Python has *dictionaries* to take care of this. See [this document](https://docs.python.org/2/tutorial/datastructures.html) for info on Python dictionaries.

	* NOTE: Indexing speeds up lookup, not insertion!
	* NOTE: Hash Tables are not sorted, so you can't iterate over them and expect that everything will be place in an order you want.
	
	2. Trees: Sorted, but lookup is a function of log(n) instead. 
	
#####Scaling Databases
	
**Too much load:** When there is too much load, replicate data from a *master* database into multiple *slave* databases. If the master can keep up with all of the writes, the slaves will handle the far more common reads.

* Downsides

	1. Doesn't help write speed
	2. "Replication lag": read hits slave before write is finished on master

**Too much data:** "Shard" the database, and break up one master into several. Example: store links 1-100 in one database, 2-200 in another, etc.

* Downsides

	1. Complex "Range queries" that hit multiple databases
	2. Joins become impossible or very difficult

Google Datastore for App Engine has some of these limitations.

#####ACID

**Atomicity**: All parts of a transaction succeed or fail together

**Consistency**: The database will always be consistent

**Isolation**: No transaction interferes with another

**Durability**: Once the transaction is committed, data won't be lost

* Takeaways

	* There are always tradeoffs that need to be made. Not all ACID properties can be fulfilled 100%
	
		* For example, replication lag causes a loss of *consistency* between the master and slave databases