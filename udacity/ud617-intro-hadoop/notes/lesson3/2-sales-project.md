#Intro to Hadoop and MapReduce

**Udacity: UD 617**

---

###Mini-Project w/ Sales Data

Now it's time for you to have a go at this. For starters, you will have to work with the same data set that we discussed in lessons. 

You will have to write some Mappers and Reducers yourself and then answer the questions about data that follow. You will have to do the data processing on your local pseudo-distributed cluster. The three questions that you have to answer about this data set are:

1. Instead of breaking the sales down by store, instead give us a sales breakdown by product category across all of our stores.
2. Find the monetary value for the highest individual sale for each separate store.
3. Find the total sales value across all the stores, and the total number of sales. Assume there is only one reducer.

When you have finished writing running your mapreduce jobs, check your understanding by seeing if you got these results:

1. Sales breakdown by product:
    * Toys = 57463477.11
    * Consumer Electronics = 57452374.13
2. Highest individual sale item in each store:
    * Chandler = 499.98
    * Reno = 499.99
    * Toledo = 499.98
3. Total sales value across all stores & number of sales
    * Number of sales = 4138476
    * Total sales = 1034457953.26

I hope you were able to get those results from your MapReduce code! If not, check out the `code/lesson3/sales-project` folder I made, which contains solutions.

Our next project will involve analyzing server log data.