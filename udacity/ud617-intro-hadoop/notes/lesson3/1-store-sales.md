#Intro to Hadoop and MapReduce

**Udacity: UD 617**

---

###Calculating Total Sales

This lesson will focus on putting what we learned about Hadoop and MapReduce to work. We're going to solve the total store sales problem we previously discussed in Lesson 2.

**Input Data**

Recall that each Mapper only recieves a portion of the input data, and will read one line at a time. The lines will look like this:

    2012-01-01  12:01   San Jose    Music   12.99   Amex
    
Note that although we would normally have to use something like [regular expressions](http://www.regexr.com/) to understand inputs (since inputs can vary), in this case each line will be delimited by the TAB character. You may notice that we have 6 pieces of data on each line. However, we are trying to calculate the total sales per store, so all we care about is finding the right key-value pair.

For our purposees, it will be best to do it like this:

* Key: Store name
* Value: Cost

**Mapper**

Here's the Python code we can use to start out:

    for line in sys.stdin:
        data = line.strip().split('\t')
        date, time, store, item, cost, payment = data
        print '{0}\t{1}'.format(store, cost)
            
Assuming that each line had 6 items to store in `data`, this code would print out the two variables that we need on every line. However, let's be a bit more [defensive](http://arstechnica.com/information-technology/2014/03/why-follow-defensive-programming-best-practice-when-code-will-never-be-public/) and make sure we can handle lines in the file that may be malformed:

    for line in sys.stdin:
        data = line.strip().split('\t')
        if len(data) == 6:
            date, time, store, item, cost, payment = data
            print '{0}\t{1}'.format(store, cost)
                
This small improvement will let us ignore lines that don't meet our requirements! Onto the mysterious step between the Mapper and Reducer.

**Shuffle and Sort**

It ensures that the values for any key are collected together, then sends the pairs of keys and values to the Reducer.

**Reducer**

In our case, we only have a single Reducer, which will get all of the keys. The data will come in like this:

    Boston  9.46
    Miami 34.99
    NYC 23.99
    

We are using something called "Hadoop Streaming", because we want to write our code in Python. [Hadoop Streaming](http://hadoop.apache.org/docs/r1.2.1/streaming.html) lets you write your MapReduce code in any language, rather than forcing you to use Java.

Something interesting to note is that all of our keys, thanks to the shuffle/sort process, will come into the Reducer in alphabetical order. That will help us decide how to go about getting running totals for each store.

We will need to keep track of 4 variables while going through the text:

* Current cost
* Current store
* Previous store
* Total sales per store

We store the current and previous stores so we can tell when we have moved on to a new key. Here's some Reducer code that will work:

    total = 0
    oldKey = None
    
    for line in sys.stdin:
        data = line.strip().split('\t')
        
        if len(data) != 2:
            continue
        
        thisKey, thisSale = data
        if oldKey and oldKey != thisKey:
            print "{0}\t{1}".format(oldKey, total)    
            total = 0
                
        oldKey = thisKey
        salesTotal += float(thisSale)
        
    if oldKey != None:
        print "{0}\t{1}".format(oldKey, total)
            
Just like with the Mapper, we recieve a line seperated by the TAB character. We're going to go through each line, keeping a running total of sales for a store. Once we move on to a new store, we first print out the total sales for the previous store. We're also sure to print out the data for the very last store once we exit the loop.

Note that this code is provided on the VM you should have set up as well, under the `code` folder in `udacity_training`. This is the actual code we will be using!

**Testing the code**

To test our code, let's head over to the VM, open the Terminal app, and go to the folder: `~/udacity_training/code`, where the Mapper and Reducer code that we wrote lives. Let's get a small sample of the full purchases file by typing this into the terminal:

    $ head -50 ../data/purchases.txt > testfile.txt
    
Now, we can use a simple pipe to send that file into our mapper code:

    $ cat testfile.txt | ./mapper.py
    
And get the desired output:

    Reno    88.25
    Chicago 31.08
    etc...
    
**Running everything**

We can simulate the entire MapReduce process right from the command line at the VM, with our new test file:
    
    $ cat testfile.txt | ./mapper.py | sort | ./reducer.py
    
If this code doesn't make sense, be sure to read up on UNIX pipes and redirection [right here](http://www.westwind.com/reference/os-x/commandline/pipes.html). This line of code gives us our store totals!

Let's run this code on the real Hadoop cluster now that we know how it works! It is always very good to test your MapReduce code locally and with a small dataset before running it on the cluster.

Before we run the code, we need to send our data file to the Hadoop cluster:

    $ hadoop fs -put /path/to/purchases.txt myinput
    
This command stores the data and names it "myinput" for later use. Now we can run the job!

    $ hs mapper.py reducer.py myinput out

In case you don't remember, `hs` was simply an alias created in [this video](https://www.youtube.com/watch?v=d5TZ_2I7dwE) to make running jobs easier.

The MapReduce job will be running, and you can check the status of the job by navigating to [http://localhost:50030/jobtracker.jsp](http://localhost:50030/jobtracker.jsp). Once everything is finished, we can see the output data:

    $ hadoop fs -cat out/part-00000 | less
    
That's all there is to it! Now, we can move on to a small project using Hadoop and the same data set.