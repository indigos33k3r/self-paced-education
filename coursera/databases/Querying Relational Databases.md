#Introduction to Databases
_Lecture 3: Querying Relational Databases_

#####Steps in Creating/Using a Relational Database
1. Design schema using DDL
2. "Bulk Load" initial data
3. Query and modify data (repeat this step)

Relational Databases support "ad-hoc" queries in high-level languages. Write complex queries without worrying about algorithms.

#####Examples
* All students w/ GPA > 3.7 applying to MIT and Stanford only
* College with highest acceptance rate in WA over the last 5 years
* All mechanical engineering applicants in Mountain View, CA

Queries return relations; have two properties:

1. Closed: getting back the same type of object you query.
2. Compositional: A second query could be posed over the answer from the first thanks to closure.
	
#####Query Langauges
1. Relational Algebra (formal language)
	* SQL (actual, implemented language)
	
Same Query in Each: IDs fo students with a GPA > 3.7 applying to Stanford

Relational Algebra
	
	π(ID)∂(GPA>3.7)^CName='Stanford'(Student ∞ Apply)

SQL

	Select Student.ID
	From Student, Apply
	Where Student.ID=Apply.ID
	And GPA > 3.7 and College='Stanford'
	

	