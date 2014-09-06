# Web Development

**Udacity: CS 253**

## Lesson 5: XML, JSON, and APIs

#####HTTP Clients

How do we make our servers speak with third parties? **HTTP**. In Python, play around with ```urllib2```.

#####XML

XML, or *Extensible Markup Language*, is a markup language not dissimilar to HTML in appearance. This is what it looks like:

	<?xml version="1.0" encoding="UTF-8"?>
	<results>
 		<itinerary>
    		<leg>
      			<origin>CUS</origin>
      			<dest>WAS</dest>
    		</leg>
  		</itinerary>
	</results>
	
The ancestor of XML and HTML, as a side note, is SGML (Standard General Markup Language), invented in the 1980s. Note that HTML5 broke the ties with SGML. 

######XML Rules

1. Every tag must have a closing tag, unlike HTML.
2. XML tags are case sensitive.
3. XML elements must be properly nested.
4. XML documents must have a root element.
5. XML attribute values must be quoted.

The rules are similar to HTML overall. XML documents that meet all of the rules are considered "well-formed".

HTML can be expressed in XML with the declaration: ```<!DOCTYPE xhtml>``` at the top.

#####Parsing XML in Python 2.7

```from xml.dom import minidom```

Note: DOM stands for "Document Object Model".

```minidom``` has a function ```parseString``` to parse XML. Structure can be made more clear in stdout using ```minidom.toprettyxml()``` on an XML object.

#####RSS

Stands for **Rich Site Summary** and **RDF Site Summary** (and also "Really Simple Syndication"). RDF stands for **Resource Description Framework**.

RSS uses a family of standard web feed formats to publish frequently updated information (news, blogs, etc.). An RSS document includes full or summarized text, as well as metadata such as publish date.

RSS uses XML format to ensure compatibility with many different machines and programs.

#####JSON

**JSON**: JavaScript Object Notation

Called this because it's valid JavaScript code. No longer associated with only JS though. In Python, import ```json```.

Possible data types are:

1. Integer
2. Floating Point
3. String
4. Boolean
5. Arrays
6. Other JSON Objects (nested inside; see below)

JSON is human-readable, and is essentially an object made up of nested key-value pairs. Here is an example:

	students = {
		"Ty" : {
			"Name" : "Ty-Lucas Kelley",
			"GPA" : 3.93,
			"Major" : "Computer Science"
		},
		"Gerry" : {
			"Name" : Gerry Pipes,
			"GPA" : 3.75,
			"Major" : "Computer Science"
		}
	}

Go to [reddit.com/.json](http://reddit.com/.json) to see a real world example of JSON.

####APIs

A lot of websites allow you to get their content in a simple way. The medium through which your software can communicate with their website is called an **API**, or *Application Programming Interface*.

Most users don't ever see or interact with an API, and lately, more sites force developers to create accounts, pay, or use OAuth to access their APIs.

Here are a few links to large sites' APIs:

1. [Twitter API](https://dev.twitter.com/)
2. [YouTube API](https://developers.google.com/youtube/)
3. [Facebook API](https://developers.facebook.com/)


**NOTE**: Always be wary of relying on 3rd party APIs. Companies fail and websites change all of the time, so you don't want to depend too much on outside websites if possible.

#####Escaping JSON in Python

Two things to remember:

1. Escape quotes using '\', a.k.a. backslash
2. All strings must be enclosed in double-quotes.

Example: 

Original: ```{"blah":["one", 2, 'th"r"ee']}```

Correct: ```{"blah": ["one", 2, "th\"r\"ee"]}```

#####Being a 'Good Citizen' on the Internet

Some rules to follow:

1. **Use a good user agent**: be honest with your request headers. Linking to your website is a good idea, in case the owner of the site you are polling needs to contact you or block you.

2. **Rate-limit yourself**: don't overload websites by sending requests one after another, with no delay.

####SOAP

Based on XML, a protocol for communicating between two machines. Not used as often now.

Very complicated, and invented by Microsoft. Alternatives include:

* Facebook's [Thrift](http://thrift.apache.org/)
* Google's [Protocol Buffers](https://developers.google.com/protocol-buffers/)
* XML
* JSON