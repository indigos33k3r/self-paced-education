#Intro to Hadoop and MapReduce

**Udacity: UD 617**

---

###Introduction

**Overview**

* Instructors
    * [Sarah Sproehnle](http://www.cloudera.com/content/cloudera/en/about/management.html), Vice President of Educational Services at Cloudera
    * [Ian Wrigley](https://www.linkedin.com/in/ianwrigley), Director of Educational Curriculum at Cloudera
* Goals
    * Learn about Big Data
    * Understand why Hadoop is useful
    * Run MapReduce jobs in Apache Hadoop
    * Write MapReduce code
* Final Project
    * Write MapReduce code to efficiently process a large web server log

**About Cloudera**

Cloudera is a company that helps develop, support, and manage the Apache Hadoop software. It also offers Apache Hadoop training to business customers.

###What are Hadoop and MapReduce?

**Hadoop**

[Hadoop](http://en.wikipedia.org/wiki/Apache_Hadoop) is an open-source software framework designed for processing large data sets. It is meant to run on clusters of low to mid-range hardware, and is developed by Apache. Hadoop is designed with the assumption that hardware failures are common and the software needs to take that into consideration.

**MapReduce**

[MapReduce](http://en.wikipedia.org/wiki/MapReduce) is both a programming model and an implementation for processing and generating large data sets on a cluster. A MapReduce program consists of two things:

1. A `Map()` function for filtering and sorting the data
2. A `Reduce()` function for performing summary operations on the filtered and sorted data.

An example of a MapReduce job would be to take a list of students, sort them by first name, and then count the frequencies of each name in the list.