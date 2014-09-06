#Introduction to Databases
_Lecture 9: Relational Algebra (1)_

###What is Relational Algebra?
* Formal query language
	* Query on a set of relations returns relation as a result
	
###Examples in this video: College Admissions Database

__Tables:__

	College(cName, state, enrollment)
	Student(sID, sName, GPA, sizeHS)
	Apply(sID, cName, major, decision)
	
###Operators

* Select
	* Denoted with sigma, picks certain rows in table
	* ex/ GPA > 3.7, applying to Stanford CS Program
	* If we want to filter two conditions, use and (^)
	
* Project
	* Denoted with pi, picks columns
	* ex/ sID, enrollment, etc.
	
* Cross Product
	* a.k.a. Cartesian Product
	* ex/ Student * Apply 	
		* Glue together the two tables
	* ex2/ Names and GPAs of students from a HS > 1000, applied to CS, and were denied
	
* Natural Join
	* Enforce equality on all attributes with same name
		* sID in Student and sID in Apply will only be combined for equal values, for example
	* Eliminate one copy of duplicate attributes
	* Written using bow tie symbol
		* Student <bowtie> Apply
	* Natural join can be duplicated using combined operators, but it simplifies things
	
* Theta Join
	 * Also expressive, not necessary
	 * Combine expressions but only keep those that pass a test
	
__To pick both rows and columns:__

* Combine operators
	* pi(condition) of (expression)
	* etc
	
###Duplicates
* ex/ List of application majors and decisions (CS: yes, CS: yes etc)
	* Relational algebra eliminates duplicates, SQL doesn't
	
###Summary
* Simplest queries: relation name
* Use operators to slice, filter, combine
* Operators: Select, Project, Cross-Product, Natural Join, Theta Join
