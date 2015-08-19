# Web Development

**Udacity: CS 253**

---

### HTTP

**Request Lines**

As we said before, HTTP (HyperText Transfer Protocol) is the main protocol of the web. It is the protocol by which clients (your browser) can communicate with servers. HTTP requests begin with something called a *request line*. Let's say we wanted to get the page at `http://example.com/foo`. The request line would look like this:

    GET /foo HTTP/1.1

This text is sent over the Internet to the server. Let's break it down:

1. Method: `GET` is the most common method; it is used to simply retrieve whatever information lies at the URL we're requesting. There are other methods as well, such as `POST`, `PUT`, and `DELETE`. In this class, we will only focus on `GET` and `POST`.
2. Path: Same as before; it's the path on the server to a file we're trying to access.
3. Version: The version of the HTTP protocol we're using. At the time of these notes, 1.1 is the standard.

Note that the host name is not in the request line; we're already connected to the host at the time the request is made.

Recall that any fragments in the URL are not part of the HTTP request!

**Headers**

The request line is followed by a bunch of headers, which are just key-value pairs that give the server some information about the request. For example:

    Host: www.example.com
    User-Agent: chrome
    Content-Type: application/json

There are many different headers, but the three above are some of the most popular ones to include in a request. They're pretty self-explanatory, but read more about them [here](http://www.w3.org/Protocols/rfc2616/rfc2616-sec14.html) if interested.

Note that the "User-Agent" header is very important. It's usually your browser, but it can be scripts or other apps you make as well; for example, an app that gets data from Reddit. Being honest with your user agent is important, and is a part of being ethical on the web. Sometimes, people use fake user agents and are trying to do malicious things on a website.

**HTTP Responses**

After your browser, application, or script sends a request to a server, the server will reply with a *response*.

Responses look pretty similar to requests:

    HTTP/1.1 200 OK

This particular response line contains the protocol version, a *status code*, and a *reason phrase*. Status codes are simply numbers that stand for something. Here are some common ones:

* 200: Request fulfilled successfully
* 201: Created after POST
* 302: Resource moved
* 404: Page not found
* 500: Server error

Generally, anything in the 200 range is good, while 400 (client) and 500 (server) are errors. 300 range status codes are for redirection (for example, when a page exists but has moved). Read more about status codes and what the mean [here](http://www.w3.org/Protocols/HTTP/HTRESP.html).

The reason phrase is simply a message associated with the status code, and is meant to be human-readable.

**Reponse Headers**

Again, just like the request, the response contains headers. Here are some common ones:

    Date: Tue Mar 2014 11:34:33 GMT
    Server: Apache/2.2.3
    Content-Type: text/html
    Content-Length: 1539

Generally, it's best practice to not include your server type; doing so simply gives potential hackers more information to work with!

**Telnet**

Open up a terminal and type `telnet www.google.com 80`, then hit enter. This will send an HTTP request to Google. We also need to include some headers, so let's use these:

    GET / HTTP/1.0
    Host: www.google.com

Hit enter twice and you should see a response like this:

    HTTP/1.0 200 OK
    Date: Sat, 20 Sep 2014 16:25:11 GMT
    Expires: -1
    Cache-Control: private, max-age=0
    Content-Type: text/html; charset=ISO-8859-1
    Set-Cookie: PREF=ID=6e8d7d0880be855a:FF=0:TM=1411230311:LM=1411230311:S=KYlDkn6DVBlfgNhh; expires=Mon, 19-Sep-2016 16:25:11 GMT; path=/; domain=.google.com
    Set-Cookie: NID=67=ZAO7Y-jbkSj0JjJSN3O2AkSIcxXe0qZbKwpeNZHjys8YHfz3dJPr0YUCKv3NwkjZENYIEwHhDY430u3tI0EYPEav_gsZdzsA7AV16GV7PnRc_vIpc6Tp-2T0yzyGxa2O; expires=Sun, 22-Mar-2015 16:25:11 GMT; path=/; domain=.google.com; HttpOnly
    P3P: CP="This is not a P3P policy! See http://www.google.com/support/accounts/bin/answer.py?hl=en&answer=151657 for more info."
    Server: gws
    X-XSS-Protection: 1; mode=block
    X-Frame-Options: SAMEORIGIN
    Alternate-Protocol: 80:quic,p=0.002

There are a lot of headers in there that we haven't talked about, but you get the idea!

**Servers & Web Applications**

The purpose of a server is to respond to HTTP requests. There are two main classifications for the type of response you'll get from a server:

1. Static: Files, images, any other type of content that is pre-written
2. Dynamic: Response is built on the fly by a running program. This is the more interesting type of content!
    * Udacity, Facebook, and almost every other website generate dynamic content based on a number of factors.

Programs that serve dynamic content are called *web applications*. This is the focus of this course!
