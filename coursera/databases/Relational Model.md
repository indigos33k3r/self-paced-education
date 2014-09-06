#Introduction to Databases
_Lecture 2: The Relational Model_

#####Quick Facts
* More than 35 years old
* Used by all major commercial database systems
* Very simple model
* Query with high-level languages
* Efficient implementations

#####Constructs
* Database: set of named relations (tables)
	* Each relation has a set of named attributes (columns)
	* Each tuple (row) has a value for each attribute
	* Each attribute has a type (domain)
		* NULL: undefined or unknown attribute
			* Need to be careful when querying when there are NULL values
			* Example: query for students with GPA > 3.5 or GPA <= 3.5... Do we get Craig?
* Schema
	* Structure of the relations in a database
* Instance
	* Actual contents
* Key
	* Attribute / set of attrubutes whose value is unique in each table
		* Example: Student ID, name/state combo for colleges

#####Example Tables
	
	Students

	|  ID  | Name  |  GPA |
	-----------------------
	| 123  | Amy   | 3.9  |
	-----------------------
	| 234  | Bob   | 3.4  |
	-----------------------
	| 567  | Craig | NULL |
	
	
	Colleges

	| Name     | State | Enrolled |
	-------------------------------
	| Stanford | CA    | 15000    |
	-------------------------------
	| MIT      | MA    | 10000    |
	-------------------------------


#####SQL Database Language
* Creating Relations/Tables:

		Create Table Students(ID, Name, GPA)
		
		Create Table Colleges(Name string, State char(2), Enrolled integer)
	
