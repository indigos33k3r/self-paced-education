#Introduction to Databases
_Lecture 10: Relational Algebra (2)_

###More Operators

* Union
	* List of college and student names
		* ex/ Stanford, Mary, Susan, Cornell, etc.
	* project(cName) College U project(sName) Student
	
* Difference
	* IDs of students who didn't apply anywhere
	* project(sID) Student - project(sID) Apply
	* What about IDs and names?
		*  project(sName)(project(sID) Student - project(sID) Apply) <bowtie> Student
		
* Intersection
	* Names that are both a college name and a student name
	* project(cName) College N project(sName) Student
	* Doesn't add expressive power:
		* e1 N e2 == e1 - (e1 - e2)
		* e1 N e2 == e1 <bowtie> e2
			* Schema needs to be the same
			
* Rename
	* Uses Greek symbol row
	* Unifies schemas for set operators
		* List of college and student names
			* cName and sName both become "name" for example
	* For disambiguation in self-joins
		* Pairs of colleges in same state


###Alternate Notations
* Assignment statements
* Expression trees  

r - s = 4 2 3, 1 2 6 U s - r 2 5 4