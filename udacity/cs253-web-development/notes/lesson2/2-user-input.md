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

If you were to open that form in a browser, you wouldn't see anything of value yet; we need to add content! We need another new HTML tag to do this: "input". The input tag is used to get, as you might imagine, input from the user. 

Just like any other tag, it can handle a bunch of attributes. However, attributes will be used to a greater effect here than we've previously seen.

* The `name` attribute: We can give our input boxes names, which will become useful soon: `<input name="hello">`
* The `type` attribute: Being able to set the type of the input (radio button, text, check box, etc) shows how versatile of a tag it is. Copy the code from below into an HTML file and open it in your browser to see a few of the many input types we can use with HTML5:

            <form>
                <input type="checkbox">
                <input type="button">
                <input type="color">
                <input type="text">
                <input type="file">
                <input type="password">
                <input type="range">
            </form>
            
I've also included a form demo in the `lesson2/code` section of these notes that you can look at.

Let's try something out! Create a file called `form.html` and inside of it, write this:

    <form>
        <input name="q" type="text">
    </form>
    
Then, open that file in your browser and type something into the box and hit Enter. You should've noticed that the URL changed! It should now look like it did before, but with this added to it: `?q=the_text_you_typed`, and the text should disappear. Remember the query parameters we talked about in lesson 1? This should be familiar.

Let's do one more thing; Change your HTML to look like this:

    <form>
        <input name="q" type="text">
        <input type="submit">
    </form>
    
If you enter some text and click "Submit", you should get the same result. That's because in both cases, we are "submitting" the form. By default, the form will just submit to itself, which basically means it does nothing. So, we need to talk about how to make the form submit somewhere else:

**The "action" attribute**

To control where our form submits itself to, we need to use another attribute called "action". This attribute just tells the form what URL to submit its data to. Let's add one:

    <form action="http://google.com/search">
        <input name="q" type="text">
        <input type="submit">
    </form>
    
Filling out the form and clicking enter should redirect you to the Google search results for your text!