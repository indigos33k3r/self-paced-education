# Web Development

**Udacity: CS 253**

---

### HTML: HyperText Markup Language

HTML documents are the heart of the web; they can do a number of things. HTML is made up of:

* Text content that you see
* Markup (what it looks like)
* References to images, videos, and other files
* Links to other HTML pages

You can experiment with HTML by going to [this website](http://jsfiddle.net/WW3bh/)!

**Plain Text**

Plain text in an HTML document is just plain text; there's nothing changed.

You can prove this by creating a new document, called `hello.html`, and filling it in like this:

    Hello, world!

If you were to open that HTML page in your browser, you'll notice that the page looks something like this:

![hello](../img/hello.png)

**Markup & Tags**

Just being able to edit plain text isn't enough though. What if we wanted bold text? That's where something called "markup" comes in. Markup is just a part of HTML that allows us to do things like make text bold, organize elements into groups, and many other things.

The way we write HTML markup is through these things called "tags". Tags look like this:

    <name>content inside tag</name>

The content inside of a tag can also contain other tags, but we won't worry about that for now. The first tag, which looked like `<name>`, is called the *opening tag*, and the second one, which has the slash inside of it, is called the *closing tag*. Here's some examples of tags: (I encourage you to try this out on your own too):

* bold: `<b>bold text</b>`
* italics: `<em>italic text</em>`
* bold and italic text: `<b><em>This text is both bold and italic because I wrapped it in two tags!</em></b>`

You have to be careful to close your tags though! If you forget to close a `<b>` tag, for example, *all* of the text that follows the `<b>` tag will be bold, even if you didn't want it to be. Things can get weird if you don't close a bunch of tags.

**Attributes**

Time to learn about a new concept! Take a look at this:

    <tag>content</tag>

Which just looks like the tags we are used to now. Now I'm going to add something new:

    <tag attribute="value">content</tag>

That thing that got plopped in the middle of the opening tag is called an *attribute*. HTML attributes have two properties:

1. A name: in the above example, I just used "attribute".
2. A value: in the above example, I just used "value".

We're going to demonstrate an example of a tag that uses attributes. These are "anchor" tags:

    <a href="http://google.com">Google</a>

If you were to render this HTML in your browser, you'd see the word "Google", which you could click on to go google.com! The tag itself works the same way as before; we're just wrapping content with them. The attribute here is called `href`, and that means "HyperText Reference".

Links aren't the only tags that can have attributes, as we will continue to see:

**Images**

To display images on our web pages, we use an image tag:

    <img src="../image.png" alt="here is some text">

There are three things I want to point out regarding image tags:

1. No closing tag: Not all elements in HTML require a closing tag. These are called "void elements", and `<img>` is our first example of one.
2. `src` attribute: This tells us the location of our image.
3. `alt` attribute: The "alternate" text is displayed if the image doesn't load.

**Whitespace**

Try rendering this in your browser:

    <b>This HTML       has lots of 
        spaces and newlines     everywhere</b>

It may look funny, but believe it or not, it'll look like this in the browser: **This HTML has lots of spaces and newlines everywhere**

This is because all unnecessary whitespace, whether it be spaces, tabs, or newlines, is trimmed in HTML. We can force our markup to have line breaks though! This is where the `<br>` tag, or "break" tag, comes in:

    First line<br>Second line

Try it out! `<br>` is the HTML equivalent of `\n` in most programming languages.

**Block vs. Inline elements**

You may have noticed before that tags like `<em>` or `<b>` didn't result in any separation between words. Check it out:

    <b>This text will be on the same line as</b><em> this text</em>.

However, let's introduce a new tag, called the "paragraph" tag, that exhibits different behavior:

    <p>One line</p><p>Second line</p>

The `<p>` tag forces separation between text because it is a "block" element. They, by default, will be placed below elements that come before them in your markup because they get their own invisible "box" with a height and width. Essentially, they get their own line. We will talk about the spacing and other things when we get to CSS later on!

Here are a few examples of inline and block elements in HTML:

* Inline
    * `<a>`
    * `<img>`
    * `<br>`
    * `<em>`
* Block
    * `<p>`
    * `<div>`
    * `<table>`

There are two other tags to mention before we move on: `div` and `span`.

The HTML `<div>` and `<span>` tags can be considered more "generic" elements than something like `<p>` or `<b>`. Span is inline, and div is block, but what you need to remember is that they simply wrap their content and can have styles applied to them using CSS. Other elements can as well, but span and div don't do anything by default, which makes them unique.

**HTML Documents**

The last part of HTML we're going to talk about for now involves making a real HTML file! All HTML (assuming we're writing [HTML5](http://en.wikipedia.org/wiki/HTML5)) files start with this line:

    <!doctype html>

This line tells the web broswer what kind of document this is. We then need to fill in the stuff below that, and you'll recognize three new tags being used:

    <!doctype html>
    <html>
        <head>
 
        </head>
        <body>

        </body>
    </html>

Before we fill in some more stuff on our new page, let's take a step back:

1. The `<html>` tag
    * This tag surrounds the entire document (except for the doctype declaration at the top).
2. The `<head>` tag
    * This part of the document includes some metadata and links to JavaScript and CSS files.
3. The `<body>` tag
    * This is where the content goes! All of the HTML elements we were learning before would go in here.

Let's fill in the document (be sure to look up any tags that don't make sense to you, as I don't feel a need to explain any more):

    <!doctype html>
    <html>
        <head>
            <title>My Website</title>
            <meta charset="utf-8">
            <meta name="description" content="This is what my site's description is.">
        </head>
        <body>
            <div>
                <p>
                    This is a paragraph with some <b>bold text</b>!
                </p>
            </div>
        </body>
    </html>

Save that file as `index.html` and open it in a web browser: that's your first complete HTML document! There's a lot more to HTML, but this course is about back end, not front end, web development, so we don't need to go too much more in-depth into HTML.

Check out these resources to learn all about HTML5:

* [HTML5Rocks](http://html5rocks.com)
* [HTML-5-Tutorial](http://html-5-tutorial.com)
* [Dive into HTML5](http://diveintohtml5.info)

Time to move on to URLs!
