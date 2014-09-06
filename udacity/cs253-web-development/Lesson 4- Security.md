# Web Development

**Udacity: CS 253**

## Lesson 4: User Accounts and Security

#####Cookies

* Small piece of data stored in the browser for a website

	* Format: name = value
	
	* Used for user ids and temporary information (ex/ logged in or not)
	
	* Cookies sent as HTTP header generally
	
	* Generally, 20 cookies or so can be stored **per website**
	
	* Must be associated with a particular domain
	
		* ex/ udacity.com can only send and store cookies associated with itself
		
	* **Size**: < 4 KB
	
	* Example uses:
	
		1. Login information
		
		2. Tracking for ads
		
		3. Small amounts of data to avoid using a database for everything
		
#####Cookie Headers

Browser Request: ```Cookie: name = value```

Server Response: ```Set-Cookie: name = value```


#####Cookie Domains

Example: ```Set-Cookie: name = steve; Domain = www.reddit.com; Path = /```

* Default path is /

* Domain
	
	* Cookie will only get sent if value of domain is correct
	
#####Cookie Expiration

```Set-cookie: user = 123; Expires = Tue, 2 Jan 2025 00:00:00 GMT```

* A cookie with no 'expires' parameter gets deleted when the browser closes. This is called a 'session' cookie.

#####Editing cookies in the browser dev tools

Open the dev tools:

* Ex/ ```document.cookie  = 'visits=1000000'```

#####Hashing

What is a hash?

* `H(x) = y`

	* x is some data
	
	* y is a fixed length bit string (32-512 bits)
	
* Properties of a good hash function

	* Very difficult to generate a specific output
	 
	* Should be impossible to find a particular x for a particular y
	 
		* Irreversible: "One-way function"
		
	* Can't modify x without significantly changing y
	
	* Little to no **collisions**: two values hashing to the same value
	
* NEVER WRITE YOUR OWN HASH FUNCTION IN PRODUCTION PURPOSES

	* There are well-tested and established functions out there already. These are organized from fastest / least secure to slowest / most secure:
	
		1. CRC32: checksums, fast, relatively insecure (lots of collisions)
		
		2. MD5: fast, popular, no longer secure (broken in 2013)
		
		3. SHA-1: fairly secure, somewhat fast
		
		4. SHA-256: secure, slow

* In Python, import `hashlib` to get the standard hash functions

		> x = hashlib.sha256('udacity')
		> x.hexdigest()
		>>> '016d473857f1029884ec80ede8ae486f33d2fdad9411d63cd2aab11097ee997c'

#####Hashing Cookies

Send ```Set-Cookie: visits = 5, <hashed value of 5>``` to browser.

This isn't always enough, so we need to hash not just the data, but instead the data + a secret string that only we know. Python's ```hmac``` module can accomplish this:

	> hmac.new('secret', 'udacity', hashlib.sha256).hexdigest()
	

#####Password Hashing

Never store passwords in plain text in a database! Instead, store a password **hash**. This way, it is nearly impossible to turn that hash back into the actual password.

Benefits:

* Very little extra work
* Data is safe if database gets compromised
* Nobody, including you, knows the users' passwords
* People unfortunately use the same password for lots of sites

Problems:

Even though hashing makes you almost 100% safe, if someone created a database of the mapping of every sha256 value to a word, they could steal passwords. This is called a [rainbow table](http://kestas.kuliukas.com/RainbowTables/). 

Adding in secrets can circumvent this, but there are better options:

#####Salts

A **salt** is a bunch of random characters that are added to the password before it is hashed. This invalidates rainbow tables.

**NOTE**: be wary of doing it yourself, and always do research on 3rd party libraries before using them first.

Here is a Python example of generating a salt:

	import random, string
	
	def make_salt():
		return ''.join(random.choice(string.letters) for x in range(5))
		
#####Bcrypt

The problem with most hashing functions is that they are designed to be *fast*, not completely secure. 

**Bcrypt** is designed to be as secure as possible, and as slow as you want it to be (takes a speed parameter).

Bcrypt is the best hashing algorithm to use when storing passwords.

#####HTTPS

With HTTPS, data is encrypted using SSL, so there is no plain text data sent between the client and server. This way, data cannot be intercepted (in most cases) by a middle man.

#####Vulnerabilities

1. XSS (Cross Site Scripting): Accepting data from a user w/o escaping it. A malicious user could insert a JavaScript function or some HTML to execute code to fetch cookies, for example.

	Solutions:
		
	* Escape HTML

2. SQL Injection: Same concept as XSS; malicious users will try to drop tables or add items to your database.

	Solutions:
	
	* No string substitution in SQL queries
	
	* Use a library like SQLAlchemy for safety
	
3. memcached Injection: Malicious users will try to pollute your cache with junk data

4. CSRF (Cross Site Request Forgery): CSRF exploits the trust a site has in a user's browser, generally to imitate other authenticated users. See the [Wikipedia](http://en.wikipedia.org/wiki/Cross-site_request_forgery) page for more info.

	Solutions:
	
	* Secrets!
	
#####Production vs Development

Store things like secrets and other global variables in a production file, to keep them hidden and safe.