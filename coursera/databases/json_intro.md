#Introduction to Databases
_Lecture 7: JSON Data_

###What is JSON?

* An newer alternative to XML and Relational Databases
* "JavaScript Object Notation" - not tied to JS though
* Made for serializing data objects, usually in files
* Human-readable, useful for data interchange
* Good for storing semi-structured data

###Basic Constructs (Recursive)

1. Base Values: Number, String, Boolean, null
2. Objects: Sets of label-value pairs, enclosed in {}
3. Arrays: Lists of values, enclosed in []

###Example JSON

* Note lack of consistent structure

	{ "Books":
	  [
		{ "ISBN":"ISBN-0-13-713526-2",
		  "Price":85,
		  "Edition":3,
		  "Title":"A Course in Database Systems",
		  "Authors": [
		  	{"First_Name":"Jeffery", "Last_Name":"Ullman"}, 
		    {"First_Name":"Jane", "Last_Name":"Widom"}  
		  ]
		},
		{ "ISBN":"ISBN-0-15-003536-6",
		  "Price":55,
		  "Remark":"Buy this book with the CD",
		  "Title":"A Course in Database Systems",
		  "Authors": [
		  	{"First_Name":"Jeffery", "Last_Name":"Ullman"}, 
		    {"First_Name":"Jane", "Last_Name":"Widom"},
		    {"First_Name":"Robert", "Last_Name":"Zealom"} 
		  ]
		}
	  ],
	  "Magazines":
	  [
	  	{ "Title":"National Geographic",
	  	  "Month":"January",
	  	  "Year":2009
	  	},
	  	{ "Title":"Newsweek",
	      "Month":"March",
	      "Year":2009
	  	}
	  ]
	}
	
###Relational Model vs JSON

1. Stucture
	* Relational: Tables
	* JSON: Nested Sets / Arrays
2. Schema
	* Relational: Fixed in Advance
	* JSON: Flexible
3. Queries
	* Relational: Simple, expressive languages
	* JSON: None widely used (JSONiq, JSON Path, JAQL)
4. Ordering
	* Relational: None
	* JSON: Arrays
5. Implementation
	* Relational: Native Systems
	* JSON: Coupled with programming languages, "NoSQL" systems
	
###XML vs JSON

1. Verbosity
	* XML: More
	* JSON: Less
2. Complexity
	* XML: More
	* JSON: Less
3. Enforced Validation
	* XML: DTDs, XSDs
	* JSON: JSON Schema
4. Programming Interface
	* XML: Clunky, "Impedence Mismatch"
	* JSON: Simple, Direct
5. Querying
	* XML: XPath, XQuery, XSLT
	* JSON: None widely used (JSONiq, JSON Path, JAQL)
	
###Syntactically Valid JSON

* Adheres to basic structural requirements
	* Sets of label-value pairs
	* Arrays of values
	* Base values from predefined types
* File -> Parser -> Objects or Errors

###Semantically Valid JSON

* Confirms to specified schema
* File + JSON Schema -> Validator -> Objects or Errors

###Summary
Useful, quick, human-readable