# Web Development

**Udacity: CS 253**

## Lesson 2: Forms and Input

* Forms
	* Using the form tag in HTML, you can create forms for user input. Here is a form that submits a query to Google Search:
	
			<form method="get" action="http://google.com/search">
				<input name="query">
				<input type="submit">
			</form>
			
* URL Encoding / Escaping
	* URL's can't have spaces and certain other symbols, so those characters are *escaped* using the % character:
		* space : %20
		* ! : %21
	* Here is a Google Search URL for the query, "I love peanut butter & jelly":
		* I+love+peanut+butter+%26+jelly
* GET v. POST
	* GET
		* Parameters in the URL
		* Most Commmon
		* Used for fetching documents
		* Limited by max URL length
		* Ok to cache
		* Not ok to change server
			* Should be able to make same request over and over again
	* POST
		* Parameters in request body
		* Used for updating data
		* No max length
		* Not ok to cache (probably updating data on server)
		* Ok to change server
* Passwords
	* In an input box in a form, change the type to "password" to keep the text hidden
	* Will NOT be hidden in the URL though! Sent in plain text

Other forms of input include dropdowns ("option"), as well as radio buttons and checkboxes.