#Introduction to Databases
_DTDs Quiz: My Solution_

#####Problem 1

__DTD__

	<!ELEMENT Course_Catalog (Department+)>
	<!ELEMENT Department (Title, Chair, Course+)>
	<!ATTLIST Department Code CDATA #REQUIRED>
	<!ELEMENT Chair (Professor)>
	<!ELEMENT Course (Title, Description?, Instructors, Prerequisites?)>
	<!ATTLIST Course Number CDATA #REQUIRED
                              Enrollment CDATA #IMPLIED>
	<!ELEMENT Instructors ((Lecturer+, Professor*) | (Professor+, Lecturer*))>
	<!ELEMENT Prerequisites (Prereq+)>
	<!ELEMENT Professor (First_Name, Middle_Initial?, Last_Name)>
	<!ELEMENT Lecturer (First_Name, Middle_Initial?, Last_Name)>

	<!ELEMENT Title (#PCDATA)>
	<!ELEMENT Description (#PCDATA)>
	<!ELEMENT Prereq (#PCDATA)>
	<!ELEMENT First_Name (#PCDATA)>
	<!ELEMENT Last_Name (#PCDATA)>
	<!ELEMENT Middle_Initial (#PCDATA)>

__XML__

[Original Document](http://s3.amazonaws.com/spark-public/db/docs/courses-noID.xml "Original Document")

#####Problem 2

__DTD__
	
	Not solved yet


__XML__

[Original Document](http://s3.amazonaws.com/spark-public/db/docs/courses-ID.xml "Original Document")

#####Problem 3

__DTD__

	<!ELEMENT countries (country*)>
	<!ELEMENT country (city*, language*)>
	<!ATTLIST country name CDATA #REQUIRED
                      population CDATA #REQUIRED
                      area CDATA #REQUIRED>
	<!ELEMENT city (name, population)>
	<!ELEMENT language (#PCDATA)>
	<!ATTLIST language percentage CDATA #REQUIRED>
	<!ELEMENT name (#PCDATA)>
	<!ELEMENT population (#PCDATA)>
	
__XML__

[Original Document](http://s3.amazonaws.com/spark-public/db/docs/countries.xml "Original Document")

