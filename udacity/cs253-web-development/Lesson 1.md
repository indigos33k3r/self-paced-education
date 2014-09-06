# Web Development

**Udacity: CS 253**

## Lesson 1 - How the Web Works

-   *Covered in this Lesson*

    -   *The Web*

        -   *Invented in the 1990s (Sir Tim Berners-Lee)*

    -   *HTML*

        -   *HyperText Markup Language*

    -   *Servers*

        -   *Computers that host the files on the web*

    -   *HTTP*

        -   *The main protocol of the web*

    -   *Web Applications*

        -   *Programs you use in your browser*

-   How the Internet Works in a Picture

    ![][]

## HTML

-   **HTML**

    -   Made up of text content, markup, references to other documents

    -   HTML markup is made up of tags: \<NAME\> content \</NAME\>

        -   Tags are also called elements, and can be nested inside of
            other tags.

        -   Forgetting to close a tag can lead to problems.

-   **Example Tags**

    -   \<b\> : bold

    -   \<em\> : emphasis / italic

    -   \<img\> : image

    -   \<br\> : break / newline

    -   \<p\> : paragraph

    -   \<h1\> : heading 1

-   **HTML Attributes**

    -   *Example 1*: \<a href="http://hello.com"\>link\</a\>

        -   ​href : attribute name

        -   "http://hello.com" : value

    -   *Example 2*: \<img src="path/to/image" alt="alternate text"\>

        -   Doesn't need to be closed! Called a *void* tag

-   **Inline / Block Elements**

    -   \<br\>, \<span\>, \<img\>, \<a\>, \<strong\> : inline

        -   Just an inserted newline character

    -   \<p\>, \<div\>, \<form\> : block

        -   invisible "box" with height and width created around text

-   **HTML Document Structure**

    ![][1]

    1.  DOCTYPE Declaration

    2.  Head : Metadata such as title, css styles, links to scripts,
        etc.

    3.  Body : Content

## URLs

-   URL: Uniform Resource Locator

    -   http://www.udacity.com/

        -   Protocol: HTTP, FTP, HTTPS

        -   Host: address of server w/ document we want (translates to
            IP Address)

        -   Path: location of file on machine

            ![][2]

-   Query Parameter (GET)

    -   http://example.com/foo?q=1&p=no

        -   q, p : name

        -   1, "no": value

    -   Separate query parameters using the & character

-   Fragment

    -   http://example.com/foo\#fragment

        -   Ignored by browser (Used for local JS or CSS)

        -   Always comes last in URL

-   Port

    -   http://localhost:8000 (or another number)

        -   default port = 80

-   An example URL containing all of these elements:
    http://example.com:8080/toys?p=foo\#hello

## HTTP

-   **HTTP Requests**

    -   Example: http://www.example.com/foo

    -   Request Line: **GET /foo HTTP/1.1** (already connected to host,
        so example.com not needed)

        -   *Method*: GET, POST

            -   GET is most common

        -   *Path*: /foo

        -   *Version*: 1.1 or 1.0

    -   More on Request Lines

        -   Headers are sent with the request line, of the form **Name:
            value**

            -   Host: www.example.com

            -   User-Agent: chrome

-   **HTTP Responses**

    -   Example: HTTP/1.1 200 OK

        -   Version: 1.1

        -   Status Code: 200

        -   Reason Phrase: OK

    -   Common Status Codes

        -   200 OK

        -   302 FOUND

        -   404 NOT FOUND (Client Error)

        -   500 SERVER ERROR

    -   Headers

        -   Date: Tue Mar 2012 04:33:33 GMT

        -   Server: Apache/2.3.3 (Don't include this)

        -   Content-Type: text/html

        -   Content-Length: 1678

## Servers

-   Purpose: To respond to HTTP requests

    -   Types of responses

        -   Static: Pre-written file that server returns

            -   Images, PDFs

        -   Dynamic: Made on the fly

            -   Web Application

            -   Facebook, Google Search, Blog

  []: img/web.png
  [1]: img/html.png
  [2]: img/urls.png
