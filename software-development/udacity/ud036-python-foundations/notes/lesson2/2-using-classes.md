#Programming Foundations with Python

**Udacity: UD036**

---

###Mini-Project: Using Classes to Send Text Messages

Let's use classes (and a cool API) to write code that will send text messages to a cell phone. We see texts and programming mix all the time in life:

* Two-factor authentication with Gmail
* Taxi drivers automatically sending texts, informing passengers of their location
* Dating websites

###Introducing Twilio

[Twilio](https://www.twilio.com/) is a service that lets us send text messages from our code to build powerful applications. Twilio has a Python package (aptly named `twilio`) that will let us do this.

`twilio` is an example of a package that is outside of the Python standard library (as Twilio is it's own company). A list of all packages outside of the standard library can be found [here](https://pypi.python.org/pypi).

**Installation**

Twilio doesn't come with Python when you download it, so we will need to download it separately. Here are instructions:

* [Mac](https://s3.amazonaws.com/udacity-hosted-downloads/ud036/How+to+install+Twilio+on+a+Mac.pdf)
* [Windows](https://s3.amazonaws.com/udacity-hosted-downloads/ud036/How+to+install+Twilio+on+Windows.pdf)

**Registration**

We will need to sign up with Twilio, to get two things:

1. A Twilio phone number
2. An API key

You can register [here](https://www.twilio.com/try-twilio).

Once you have your API key and Twilio phone number, we are ready to begin using the Twilio package!

###Using Twilio

There's some sample code available on Twilio's website. Let's modify it and use it:

	from twilio.rest import TwilioRestClient
	import os
 
	account_sid = os.environ['TWILIO_ACCOUNT'] #replace with your twilio account number
	auth_token  = os.environ['TWILIO_API_KEY'] #replace with your twilio auth token
	client = TwilioRestClient(account_sid, auth_token)
 
	message = client.messages.create(body="This is a test message! Hello.",
		to = os.environ["CELL_PHONE_NUMBER"], # Replace with your phone number
		from_ = os.environ["TWILIO_PHONE_NUMBER"]) # Replace with your Twilio number
		
	print message.sid
	
As far as the `os.environ` stuff, I've hidden my API key and other information by storing it in something called *environment variables*, which I can access on my computer. You can learn more about these [here](http://en.wikipedia.org/wiki/Environment_variable). Basically, I didn't want to reveal my API key and phone number in these notes.

Running the code will send a text to your phone! Cool stuff.

###Why that Mattered

You may be wondering what the relevance of using Twilio to send a text was. Look back into the code, and you will notice a few things:

1. Importing a class from a module: `from twilio.rest import TwilioRestClient`
2. Using a class: `client = TwilioRestClient(account_sid, auth_token)`
3. Class methods: `message = client.messages.create`

This is all stuff that should look familiar to us, now that we've played around with Turtle graphics and Twilio. We are using a class called `TwilioRestClient`, creating an instance of it called `client`, and calling class methods like `messages.create`. Same old, same old at this point.

For more about the `from` keyword, see [this](http://www.tutorialspoint.com/python/python_modules.htm).

If you're interested, check out the Twilio source code [on GitHub](https://github.com/twilio/twilio-python), which is a website for sharing open-source code (it has other purposes too that we won't worry about, like [version control](http://git-scm.com/book/en/Getting-Started-About-Version-Control)).

Time to move on to the last project to explain using classes!