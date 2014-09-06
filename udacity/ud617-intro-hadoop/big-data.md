#UD 617: Intro to Hadoop and MapReduce

**Udacity**

---

###Lesson 1: Big Data

**Data Sources**

According to IBM:

> "Every day, 2.5 billion gigabytes of high-velocity data are created in a variety of forms, such as social media posts, information gathered in sensors and medical devices, videos and transaction records."

* Data is everywhere:
	* AT&T can use the data from your phone to figure out where they have dead zones in their coverage.
	* To serve more targeted advertisements and suggestions on their site, Amazon uses data such as:
		* Where you are viewing from
		* What products you have viewed
		* What you purchase

Two problems arise from this massive quantity of data:

1. Storage
2. Processing

**Big Data**

There is no one definition for "Big Data", but it can be used to describe data sets so large and complex that they cannot be processed on one machine using traditional statistical software.

* Challenges of Big Data:
	1. A large amount of data is not needed
	2. Data is created at an incredibly fast pace
	3. Data comes from different sources, in different formats

* The ["Three Vs"](http://blogs.gartner.com/doug-laney/files/2012/01/ad949-3D-Data-Management-Controlling-Data-Volume-Velocity-and-Variety.pdf) of Big Data:
	* **Volume**
		* The cost of storing data has been coming down considerably:
			* 1980: > $100,000 per GB
			* 2013: $0.10 per GB
		* However, storing data *reliably* is still quite expensive. This high cost puts a cap on the amount of data a company or individual can store. However, deciding which data is important can be a challenge.
		* Data worth storing can be in the form of:
			* Transaction data
			* Internal business data
			* User data
			* Social media
			* Sensor information from hardware (such as a phone's gyroscope)
			* Medical records and information
			* Server logs
			* etc...
	* **Variety**
		* Much of the data dealt with these days can't fit into one type of pre-defined [database table](http://en.wikipedia.org/wiki/Table_(database)); this is referred to as "unstructured" or "semi-structured" data. Consider a bank's data:
			* Credit card transactions
			* Customer service records
			* Receipts
		* This data is all very different, and needs to be handled in different ways.
		* Sometimes the most unlikely data can be useful. Consider this problem:
			* A conventional system for coordinating logistics might have the nearest truck sent to a shipping center to pick up a package for delivery. However, problems might exist with that strategy: the truck could be full, the traffic could be moving slowly on the closest truck's route, etc. Instead of taking a naive "closest truck" approach, the available data could be used to pick the best option:
				* Each trucks' GPS data
				* Current route plan for each truck
				* Load of each truck
				* Fuel efficiency of each truck
				* Traffic information
	* **Velocity**
		* Data arrives at a rate of terabytes per day in some cases. Much of it can be useful though, so companies have to be careful not to throw too much away. Consider an e-commerce website:
			* Knowing that a user browses the website with a 1st-generation iPad could be a chance to offer suggestions to upgrade to the latest model.
			* Knowing the time a user spends on each item's page could lead to sending notifications to that user when items they view for a long time are on sale.

**Origins of Hadoop**

Hadoop was created by [Doug Cutting](http://en.wikipedia.org/wiki/Doug_Cutting) and [Mike Cafarella](http://en.wikipedia.org/wiki/Mike_Cafarella) in 2005. Cutting was at Yahoo at the time, working on an open source search engine called [Nutch](http://nutch.apache.org/). The Nutch team was struggling, however, due to problems concerning scalability and reliability. Around that time, Google published papers about their [distributed file system (GFS)](http://static.googleusercontent.com/media/research.google.com/en/us/archive/gfs-sosp2003.pdf) and their processing framework, [MapReduce](http://static.googleusercontent.com/media/research.google.com/en/us/archive/mapreduce-osdi04.pdf). Cutting and Cafarella wanted to implement these systems in open source, so everyone could use them. Yahoo showed interest in the project, and it became known as Hadoop. Once it got to the point of reliable processing and scalability, many companies began to adopt it.

The name "Hadoop" comes from a toy elephant that Doug's son played with all the time. Doug overheard his son calling the elephant by the name "Hadoop", so he wrote it down in case he ever needed a name for a software project.

**Core Hadoop**

The core Hadoop project consists of:

1. A way to store data: HDFS
2. A way to process data: MapReduce

The key concept is that the data is split up and stored on a cluster of machines, and then processed "in-place" on the cluster. The clusters do not need to be high end; in fact, most Hadoop clusters have mid-range hardware.

**Hadoop Ecosystem**

* Hadoop has a very large and complex ecosystem. As Hadoop has grown, the number of software projects built around it has grown too. These software projects are designed to:
	* Make Hadoop easier to use
	* Make it easier to load data into the Hadoop cluster

![Hadoop Ecosystem](http://1.bp.blogspot.com/-7Aa8EdQ2zAg/UheKFCHZHCI/AAAAAAAAB-g/AFvNNn3pA_Q/s1600/Hadoop_ecosystem.png)

* Here is information on some of the tools that are a part of the Hadoop ecosystem:
	* [Pig](http://www.cloudera.com/content/cloudera/en/resources/library/training/introduction-to-apache-pig.html) is a simple-to-understand data flow language used in the analysis of large data sets. Pig scripts are automatically converted into MapReduce jobs by the Pig interpreter, so you can analyze the data in a Hadoop cluster even if you aren't familiar with MapReduce.
	* [Hive](http://www.cloudera.com/content/cloudera/en/resources/library/training/introduction-to-apache-hive.html) enables analysis of large data sets using a language very similar to standard ANSI SQL. This means anyone who can write SQL queries can access data stored on the Hadoop cluster.
	* [HBase](http://www.cloudera.com/content/cloudera/en/resources/library/training/intorduction-hbase-todd-lipcon.html) is the database that Hadoop uses. HBase differs from a traditional relational database in that it is built to be distributed by design. The system is architected to leverage the cost-effective capabilities of Hadoop and an EDH and utilize the storage, memory, and CPU resources of any number of servers within a cluster so that the database scales horizontally as load and performance demands increase.
	* [Mahout](http://mahout.apache.org/) is an open-source and scalable machine learning library.
	* [Impala](http://www.cloudera.com/content/cloudera/en/products-and-services/cdh/impala.html) is a massively parallel processing (MPP) SQL query engine that runs natively in Hadoop. It enables users to directly query data stored in HDFS and HBase without requiring data movement or transformation.