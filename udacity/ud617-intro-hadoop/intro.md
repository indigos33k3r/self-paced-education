#UD 617: Intro to Hadoop and MapReduce

**Udacity**

---

###Introduction

**Goal of the Course**

To be able to write a MapReduce program that efficiently processes a very large web server log.

**Instructors**

* [Sarah Sproehnle](https://www.linkedin.com/profile/view?id=3951654&authType=name&authToken=ACpB&trk=prof-sb-browse_map-name), VP of Educational Services at Cloudera
* [Ian Wrigley](https://www.linkedin.com/in/ianwrigley), Director of Educational Curriculum at Cloudera

**What is Big Data?**

"Big Data" is a term used to describe any collection of data sets so large that it becomes hard to process and understand using traditional data processing applications.

**What is Hadoop?**

[Hadoop](http://hadoop.apache.org) is an open source software library by [Apache](http://apache.org) that allows for the distributed processing of large data sets across clusters of computers. The Hadoop project contains several modules:

1. Hadoop Common: The common utilities that support the other Hadoop modules.
2. Hadoop Distributed File System (HDFS): A distributed file system that provides high-throughput access to application data.
3. Hadoop YARN: A framework for job scheduling and cluster resource management.
4. Hadoop MapReduce: A YARN-based system for parallel processing of large data sets.

**What is MapReduce?**

[MapReduce](http://en.wikipedia.org/wiki/Mapreduce) is a programming model and implementation for processing and generating large sets of data with a parallel/distributed algorithm on a cluster. A MapReduce program consists of:

* A `Map()` procedure that performs filtering and sorting on the data set
* A `Reduce()` procedure that performs a summary operation, such as counting the frequency of a certain name in a data set