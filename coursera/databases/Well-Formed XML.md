#Introduction to Databases
_Lecture 4: Well-Formed XML_

#####Extensible Markup Language (XML)
* Standard for data representation and exchange
* Alternative to relational model
* Similar to HTML in terms of appearance
	* Tags describe content instead of formatting
	
#####Example XML Document

	<?xml version="1.0">
	<!-- Bookstore with no DTD -->
	<Bookstore>
		<Book ISBN="ISBN-0-13-713526-2" Price="85" Edition="3rd">
			<Title>A First Course in Database Systems</Title>
			<Authors>
				<Author>
					<First_Name>Jefferey</First_Name>
					<Last_Name>Ullman</Last_Name>
				</Author>
				<Author>
					<First_Name>Jennifer</First_Name>
					<Last_Name>Widom</Last_Name>
				</Author>
			</Authors>
		</Book>
		<Book ISBN="ISBN-0-16-713998-3" Price="45">
			<Title>Harry Potter: The Chamber of Secrets</Title>
			<Authors>
				<Author>
					<First_Name>J.K.</First_Name>
					<Last_Name>Rowling</Last_Name>
				</Author>
			</Authors>
		</Book>
	</Bookstore>

#####XML Breakdown

1. Tagged Elements (nested)
		
		<First_Name>
			etc
		</First_Name>
		
2. Attributes (contained in opening tag)

		<Book ISBN="45243525" Price="85" Edition="3rd">
			etc.
		</Book>
		
3. Text (strings inside tags)


		<Title>Harry Potter</Title>
		
#####XML vs. Relational Model

1. Structure
	* XML: Hierarchical Tree
	* Relational: Tables
2. Schema
	* XML: Flexible
		* Lack of Edition in Book 2
		* Different Numbers of Authors
	* Relational: Fixed in Advance
3. Queries
	* XML: Not so simple
	* Relational: Simple languages; SQL
4. Ordering
	* XML: Implied
		*  Due to top -> bottom structure of document
	* Relational: Unordered
5. Implementation
	* XML: Add-on layer over relational database
	* Relational: Native
	
#####Well-Formed XML

* Adheres to basic structural requirements
	* Single Root element
	* Matched tags, proper nesting
	* Unique attributes within elements

* XML Parser
	* Checks if XML document is well-formed

#####Displaying XML

* CSS, XSL languages
	* CSS/XSL interpreter + XML parser uses rules to generate HTML document to render in document
	
#####Conclusion
* Standard for data representation and exchange
* Formal XML specification is enormous; we will cover most important ones only 	