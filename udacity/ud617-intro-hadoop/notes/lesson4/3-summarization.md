#Intro to Hadoop and MapReduce

**Udacity: UD 617**

---

###Summarization Patterns

Summarization patterns give you a quick, high-level summary of your data. We will focus on two aspects of summarization: indexing and numerical summarization.

**Inverted Index**

An inverted index is like the index in the back of a book, or what Google uses to display search results; it's a mapping of content to a location. Indexing allows for faster searching through text. Let's say you have a book; you could find a particular word in the book in two ways:

1. By flipping through every page of the book until you see it.
2. Looking at the index in the back of the book, and directly going to the page that contains the word.

Obviously, option two takes less time, and shows the value of building an index. We're going to build our own index, again using data from the forums. You can download the dataset [here](); Try to see if you can get these answers to these questions:

1. How many times was the word "fantastic" used on the forums?
2. CSV of nodes the word "fantastically" can be found?

**Numerical Summarizations**

> "Show me the numbers" -Your Boss

Numerical summarizations include any number we can generate to summarize our data set: mean, max, min, mode, counts, etc. We might want to do a count of words, like we did with the server logs project. We might want to find the standard deviation of a set of data, which is more advanced but also under the "numerical summarization" umbrella.

Let's try to find out if there is a correlation between the day of the week and the amount of money people spend on things. The Mapper will be pretty simple; all it has to do output the day and money spent. All of the math (finding the averages) is left up to the reducer. We can do that using this MapReduce code:

Mapper:

    import sys
    from datetime import datetime
    
    for line in sys.stdin:
        data = line.strip().split("\t")
        if len(data) == 6:
            weekday = datetime.strptime(data[0], "%Y-%m-%d").weekday()
            sale = data[4]
            print = "{0}\t{1}".format(weekday, sale)
            
Reducer:

    count = 0
    oldKey = None
    totalSales = 0

    for line in sys.stdin:
	   data_mapped = line.strip().split("\t")
	       if len(data_mapped) != 2:
		      continue

	   thisKey, thisValue = data_mapped

        if oldKey and oldKey != thisKey:
            print oldKey, "\t", totalSales / count
            oldKey = thisKey
            count = 0
            totalSales = 0

        oldKey = thisKey
        count += 1
        totalSales += float(thisValue)

    if oldKey != None:
        print oldKey, "\t", totalSales / count
        
**Combiners**

This is the phase between the Mapper and Reducer. Recall the problem we just solved; calculating the average spending per day of the week. This could get quite slow and costly if we had a lot of data. That's where combiners come in.

Combiners allow us to do some of the reduction before the data gets sent off to the reducer phase, which can save a lot of network bandwidth on a real Hadoop cluster.

To use a combiner, you will have to add a new shortcut command to your VM.

In the terminal window type

    gedit ~/.bashrc

In the editor that opens, find a function definition "run_mapreduce". Copy the contents and create a new function (within the same file), let's say "run_mapreduce_with_combiner". Add the following "-combiner $2" right after "-reducer $2".

And at the end of the file, add a line for the alias:

    alias hsc=run_mapreduce_with_combiner

(or whatever you called that function). You can also change the alias itself, just make sure you are not trying to use any already existing Linux command names.

Now save the file and exit the gedit program. Run the following in the terminal:

    source ~/.bashrc

This will reload the configuration file you just edited, and your new alias should be ready to use. 

The new alias will take the second parameter (which  is the reducer script) and also use it for combiner. If you want, you can actually make another alias, that allows you to use a different script for combiner. You would need to also -upload it, same as you did for mapper and reducer scripts.