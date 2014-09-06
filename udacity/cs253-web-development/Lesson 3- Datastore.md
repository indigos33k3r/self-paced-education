# Web Development

**Udacity: CS 253**

## Lesson 3: Google App Engine Datastore

#####Tables

Called **entities**:

* Columns are not fixed

* All have an ID

* Notion of parents and ancestors

	* Relationship to other entities

#####SQL -> GQL

Simplified version of SQL that only works in the Datastore

* All queries begin with ```SELECT *```

* No joins

* No arbitrary queries: all are indexed (these are Google's machines after all).

#####Other Details

* Datastore is shared and replicated, so scaling is not a worry

* Queries are quick, because they have to be simple

* Will have to worry about consistency

#####Datastore Types

* Integer, float, string (< 500 chars, indexed), date, time, text (> 500 chars, not indexed), datetime, email, link, postal address, etc. are all offered as types in Google Datastore