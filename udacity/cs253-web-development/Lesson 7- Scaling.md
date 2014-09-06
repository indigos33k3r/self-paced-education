#Web Development
**Udacity: CS 253**

##Lesson 7: Scaling

#####Code Organization

Comes from experience; there's no correct way to organize files and folders.

However, most web projects follow a similar form (for example, MVC). Here is an example project structure, using App Engine:

	/project
		main.py (imports, url mapping)
		handler1.py
		handler2.py
		/templates
			base.html
			stuff.html
		/static
			/css
			/js
			/img
		/lib
			/db
				Post
				Art
				ORM (object relational mapping)
			/utils
				random functions and files that have no dependencies

#####Hosting

Google App Engine isn't suitable for everything (such as Ruby code, for example). Here are some other options:

1. Locally

	* This is bad for anything more than one user. Not always on, IP may change, not always accessible.
	
2. Co-locate (High effort)

	* Buy a rack of servers in a datacenter, and pay rent, per machine / bandwidth, etc.
	
		* Pros: Control over machines
		
		* Cons: Lots of work
		
3. Managed Hosting (Medium effort)

	* Rackspace, AWS, Linode, etc. Rent machines by the hour
	
		* Pros: Very little work, no worrying about bandwidth (pay per use). The host will spin up more machines for you as needed. Essentially no system administration or dealing with hardware.
		
4. Completely Managed (Little effort)

	* No effort at all. Examples are App Engine, Heroku, etc. Less customization options. Udacity uses App Engine, for example.
	
#####Frameworks

We've been using App Engine's ```webapp2``` in this course. It makes things like requests and parsing very easy. There are frameworks that give you varying degrees of control.

Features to look for are:

1. Direct access to GET / POST
	
2. Direct access to Request Headers

3. URL Mapping

Avoid "magic": you should want to know what is going on when using a framework.

As far as templates are concerned, just avoid using too much code and login inside of a template.