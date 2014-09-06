#Introduction to Databases
_Lecture 8: JSON Demo_

###JSON (Bookstore)
__Both books and magazines are arrays of two objects in this case__

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
	
###JSON Schema (Example)

	{
		"title": "Example Schema",
		"type": "object",
		"properties": {
			"firstName": {
				"type": "string"
			},
			"lastName": {
				"type": "string"
			},
			"age": {
				"description": "Age in years",
				"type": "integer",
				"minimum": 0
			}
		},
		"required": ["firstName", "lastName"]
	}