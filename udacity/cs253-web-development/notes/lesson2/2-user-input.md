# Web Development

**Udacity: CS 253**

---

### Handling User Input

This lesson will focus on forms: the text areas, check boxes, and other fields that allow websites to gather information from their users. We will begin by learning about forms and handling user input, and then focus on some good practices like escaping HTML and validation to make sure that the input is safe to accept.

**Forms**

![form](../img/form.png)

Forms are everywhere on the Internet. They are how we can get data from a client to the server. Remember the HTML tags from Lesson 1? We have another tag called `<form>`, which is used to create HTML forms. They look like this:

    <form>
        content goes here!
    </form>

If you were to open that form in a browser, you wouldn't see anything of value yet; we need to add content!

* `<input>`: The input tag is used to get, as you might imagine, input from the user. Just like any other tag, it can handle a bunch of attributes. However, attributes will be used to a greater effect here than we've previously seen.
    * The `name` attribute: We can give our input boxes names, which will become useful soon: `<input name="hello">`
    * The `type` attribute: Being able to set the type of the input (radio button, text, check box, etc) shows how versatile of a tag it is. Copy the code from below into an HTML file and open it in your browser to see a bunch of HTML tags in use:
