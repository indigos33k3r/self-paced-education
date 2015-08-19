# JavaScript Basics

**Udacity: UD 804**

---

### Variables and data

Now that you've got some exposure to JavaScript, let's start using it as a programming language.

**Variables**

The syntax for storing data in a variable looks like this:

    var name;
    name = "Ty Kelley";
    
    var age = 19;
    age = 20;
    console.log(age); //prints 20
    
This should look familiar if you've programmed before; however, there are some things to note:

1. `var` keyword for all variables: unlike Python, which requires no special keyword for declaring variables, and unlike Java or C, which require you to state the type (int, char, boolean, etc) of the variable, JavaScript uses "var" no matter what. Now, that doesn't mean JS doesn't have types; here's a list explaining types in JavaScript:
    * Primary Data Types:
        * String
        * Boolean
        * Number (all numbers are 64-bit floating point)
    * Composite Data Types:
        * Object (similar to Python dict)
        * Array
    * Special Data Types:
        * Undefined
        * Null
2. You can declare a variable with out assigning it right away. It is legal to say `var age;` and then assign it to a value in a separate statement.

Try playing around with variables in your console!

**Strings**

A string is a chain of zero or more Unicode characters, enclosed by single or double quotes. We use strings to represent text in JavaScript. Here are some examples of strings:

    "Hello, World"
    'a'
    ""
    "I've been working on the railroad"

With that being said, there are some useful built-in functions for strings that we can use! One we will talk about is `replace`. This function, which can be read about [here](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String/replace), takes two arguments (in it's simplest form): a string to find, and a string to replace it with. For example:

    var s = "I am a cool ice cream."; //this doesn't make sense
    s = s.replace("ice cream", "person");
    
    console.log(s); //prints "I am a cool person."
    
Note: I had to reassign `s` to actually change it's value!

**Back to the résumé**

Before we learn more, let's apply what we know to the project. We're going to add our name and job to the header of our résumé.

In `index.html`, take a look at this section:

    <div id="header" class="center-content">
        <ul id="topContacts" class='flex-box'></ul>
    </div>

Notice how it's lacking content? We're going to fix that with JavaScript and jQuery. Open up `helper.js` and take a look:

    var HTMLheaderName = "<h1 id='name'>%data%</h1>";
    var HTMLheaderRole = "<span>%data%</span><hr/>";

We're going to be using a combination of the `replace` function and [jQuery's `append`](http://api.jquery.com/append/) function to add our name and job/role to the document. You're going to want to replace the "%data%" with your own information, and then append it to the header section in the HTML.