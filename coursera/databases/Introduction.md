#Introduction to Databases
_Lecture 1: Intro to the course_

#####Database Management Systems

Seven Properties:

* Massive
	* Handle terabytes of data every day. More data than can fit on one computer system's hard drive.
* Persistent
	* Data in the database outlives the programs that execute on that data; multiple programs will often operate on the same data
* Safety
	* Guarantee that data will be consistent in spite of power outages, malicious users, software/hardware failures.
* Multi-User
	* Multiple programs and multiple users can read the data concurrently. Handling of this is called _concurrency control_. 	 
* Convienience
	 * Easy to work with large amounts of data. 
	 	* _Physical data indepedence_: Data storage is independent of the way programs view that data. 
	 	* _High-level query languages_: Describe what is wanted from the database, without describing the algorithms.
* Efficient
	* Thousands of querys/updates per second (not simple either), over gigantic amounts of data.
* Reliability
	* Need 99.9999% uptime in a DBMS
	
#####Not Covered in the Course

1. Ruby on Rails, Django, etc. are frameworks used to program a database application.
2. Application servers, web servers help applications communicate with databases.
3. Data-intensive applications may not use DBMS at all

#####Key Concepts

1. Data Model
	* Relational, Graph
2. Schema (type) vs. Data (variable)
	* Schema: structure of the database
	* Data: information stored in database that adheres to the schema
3. Data Definition Language (DDL)
	* Set up the schema for a database
4. Data Manipulation Languate (DML)
	* Used to query and modify the database
	
#####Key People

1. DBMS Implementer
	* Builds system
2. Database Designer
	* Establishes schema
3. Database Application Developer
	* Programs that operate on database
4. Database Admin
	* Loads the data, keeps database running correctly
	
#####Conclusion
Databases are everywhere!