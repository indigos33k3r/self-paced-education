#Introduction to Databases
_Lecture 6: XML Schema_

#####XML Schema
* Extensive Language
* Like DTDs, can specify elements, attributes, nesting, order, etc.
* Also data types, keys, typed pointers, etc.

__XSD is written in XML__

#####Example

![XML Schema](images/schema-example.png "XML Schema")

#####XSD vs DTDs

__Typed Values__

In DTDs, everything is a string. Here, values can have types:

	<Book ISBN="ISBN-0-524353-12-3" Price="100">
		etc.
	</Book>
		
In the XSD:

	<xsd:attribute name="Price" type="xsd:integer" use="required" />
		

__Keys__

In DTDs, IDs could be specified, which were globally unique identifiers for specific elements.

In XSD, keys specify that an attribute or element value must be unique within the elements of the same type:

	<xsd:key name="BookKey">
		<xsd:selector xpath="Book" />
		<xsd:field xpath="@ISBN" />
	</xsd:key>
	
In the XML, ISBN must be a key:

	<Book ISBN="ISBN-0-524353-12-3" Price="100">
		etc.
	</Book>

__References__

Effectively, typed pointers. Called a "keyref":

	<xsd:keyref name="BookKeyRef" refer"BookKey">
		<xsd:selector xpath="Book/Remark/BookRef" />
		<xsd:field xpath="@book" />
	</xsd:keyref>
	
In the XML

	<Remark>
		Amazon.com says: Buy this book bundled with
		<BookRef book="ISBN-0-13-452352-4" /> - a great deal!
	</Remark>
	
__Occurence Constraints__

In the XML Schema, we can specify min and max # of occurences. Default is 1.

	<xsd:element name="Book" type="BookType"
					minOccurs="0" maxOccurs="unbounded" />
	<xsd:element name="Author" type="AuthorType"
					minOccurs="0" maxOccurs="unbounded" />
					
minOccurs, maxOccurs, both, or niether can be specified.


	