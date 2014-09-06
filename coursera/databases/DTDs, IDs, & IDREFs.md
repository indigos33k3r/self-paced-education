#Introduction to Databases
_Lecture 5: DTDs, IDs, and IDREFs_

#####Valid XML
* Adheres to same requrements as well-formed XML
* Also adheres to content specific specification

Validating XML Parser

* Using DTD or XSD, returns "Not Valid" or parsed XML document

#####Document Type Descriptor (DTD)
* Grammar-like language for specifying elements, attributes, nesting, ordering, number of occurences, etc.
* Also special attribute types ID and IDREF(s)

#####DTD/XSD (strong typing) vs. Well-Formed (loose/no typing)

Positives

* Programs adhere to structure
* Programs are not doing any error-checking
* CSS/XSL
* Specification Language for data exchange
	* What XML needs to look like)
* Documentation

Negatives

* Less Flexibility
* DTDs can be messy for irregular data
* XSDs can be even messier than DTDs

#####DTD Example

Use with a program such as [XML Lint]("http://xmlsoft.org/xmllint.html")
	
	<!DOCTYPE Bookstore [
		<!ELEMENT Bookstore (Book | Magazine) *>
		<!ELEMENT Book (Title, Authors, Remark?)>
		<!ATTLIST Book ISBN CDATA #REQUIRED
					    Price CDATA #REQUIRED
						Edition CDATA #IMPLIED>
		<!ELEMENT Magazine (Title)>
		<!ATTLIST Magazine Month CDATA #REQUIRED
					Year CDATA #REQUIRED>
		<!ELEMENT Title (#PCDATA)>
		<!ELEMENT Authors (Author+)>
		<!ELEMENT Remark (#PCDATA)>
		<!ELEMENT Author (First_Name, Last_Name)>
		<!ELEMENT First_Name (#PCDATA)>
		<!ELEMENT Last_Name (#PCDATA)>
	]>
	
What the Constructs (Regex) means:

* '*' = Zero or more instances
* '?' = Optional component
* '|' = OR operator
* ',' = Specified order
* '+' = One or more instances
* 'PCDATA' = String for data
* 'CDATA' = String for type of attribute
* 'REQUIRED' = Required component


#####IDs and IDREFs

Properties

* Unique in document
* Similar to HTML IDs
* Pointers are untyped

"HG" is an ID in this snippet:

	<Author Ident="HG">
		<First_Name>Hector</First_Name>
		<Last_Name>Gomez</Last_Name>
	</Author>
	
And further up in the document, we can use a reference to the ID to credit Hector Gomez as an author of the book "Database Systems":

	<Book ISBN="ISBN-0-13-665436-3" Price="87" Authors="HG JU JW">
		title, remark, etc... don't need to include authors now!!!
	</Book>
	
The DTD would now look like:

	<!DOCTYPE Bookstore [
		<!ELEMENT Bookstore (Book* | Author*) *>
		<!ELEMENT Book (Title, Remark?)>
		<!ATTLIST Book ISBN CDATA #REQUIRED
					    Price CDATA #REQUIRED
						Authors IDREFS #REQUIRED> <--- Note this 'S' implies singular or plural amount!!!!
		etc...
	]>
	
