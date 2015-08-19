#Intro to Hadoop and MapReduce

**Udacity: UD 617**

---

###Big Data

Companies have been collecting data for a long time. However, with the rise of the internet, the amount of data being generated, collected, and analyzed has exploded. Take this quote from [IBM](http://ibm.com):

> "Every day, 2.5 billion gigabytes of high-velocity data are created in a variety of forms, such as social media posts, information gathered in sensors and medical devices, videos and transaction records"

In fact, IBM also estimates that over 90% of the world's data has been generated *after 2012*. This is a staggering pace. Here are a few examples of data generation and collection:

1. Cell phones
    * Companies like AT&T and Verizon can use a combination of data about your cell phone's location and signal strength to figure out where they have dead zones in their coverage.
2. Web surfing
    * Amazon and Netflix, among many other internet companies, log what pages you view on their sites (and the times/duration you view them) to offer suggestions to you. Multiply this by the number of users you have, and you get a ton of data to sift through.
3. Medical Records
    * Research to cure diseases like cancer, based on patients' medical records, is constantly being performed.
    
The massive amount of data available to companies and individuals can be a good thing. However, it creates a huge problem: *we have to be able to store and process all of this data*.

**What is "Big Data"?**

There's no denying that "Big Data" is a buzzword in this day and age. Not everything is Big Data, so we will define it like this:

> "Big Data can be used to describe data sets so large and complex that they become difficult to work with using standard statistical software running on one computer." - Adapted from the [Journal of Internet Science, 2012](http://www.ijis.net/ijis7_1/ijis7_1_editorial.pdf)

Here are some things we can consider "Big Data":

* All of the orders accross hundreds of retailers
* Every stock transaction on the NYSE
* Climate data for the entire globe

Here are some things that aren't "Big Data":

* All transactions for one online store
* The server log for one website
* Information on high school kids in one town

###The "Three Vs" of Big Data

There are many challenges of Big Data:

1. Sheer amount of available data
2. Data is created at a fast pace
3. Data comes from different places, in different formats

We can describe those challenges using something called the "three Vs": velocity, volume, and variety. These terms first came about in a [2001 paper by Douglas Laney](http://blogs.gartner.com/doug-laney/files/2012/01/ad949-3D-Data-Management-Controlling-Data-Volume-Velocity-and-Variety.pdf). Let's talk about volume first:

**Volume**

Volume refers to the *size of the data* set you're dealing with. 

The price of storing data has decreased sharply over the last decade, and continues to do so every year. For some perspective:

    1980: > $100,000 / GB
    2013: < $0.10 / GB
    
That's pretty impressive! There's a catch though: storing data *reliably* is still pretty expensive. This cost barrier puts a cap on the amount of data a company can store. This is a problem because so many different types of data can be helpful to a company:

* Transactions
* Social media
* Hardware sensors
* Medical records
* Internal business information
* Server logs
* etc...

Since it can be too difficult to decide which data is the most important, what we need instead is a more afforable way to store (and access) our data reliably.

**Variety**

This is our second "V"; it means that data comes from many different sources, and in different formats. This creates a problem for the old way of doing things, which was to use SQL (and other relational) databases. 

[Relational databases](http://en.wikipedia.org/wiki/Relational_database) require that all data can fit into a pre-defined table with a strict set of rules. That's not so fun when you have terabytes of data coming in from all over the place.

This type of data, which may not bode well for relational databases, is called "unstructured" data. For example, a bank may have:

* A list of your credit card transactions
* Recordings of customer service calls
* Account information like name and phone number

What is nice about Hadoop is that it *doens't care about how you store your data*: you can store it as it arrived, and manipulate it later. Being able to store a variety of data is incredibly useful. Take this problem:

* A conventional system for coordinating shipping center logistics may simply send the closest truck to a warehouse to pick up packages. This may not always be the best option though! Here's other data that could be helpful:
    * Truck location
    * Routes for each truck
    * Traffic data
    * Number of packages each truck has already
    * Fuel efficiency
    
**Velocity**

We need to be able to store and process data as it arrives. Think about an e-commmerce website, and the value that instantly being able to process user data has:

* If you view a product for 5 minutes straight, we could send you emails informing you of sales on similar products.
* We could send you promotions for new iPads if we know you browse our site with a 4-year old tablet.

This ability to process data on the fly can easily result in bigger profits for companies!

Now, let's talk about Apache Hadoop and its origins.