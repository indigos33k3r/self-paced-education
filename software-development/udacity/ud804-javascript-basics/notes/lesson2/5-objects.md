# JavaScript Basics

**Udacity: UD 804**

---

### Objects

Remember how we could get the length of an array by saying `myArray.length`? That's because arrays are a special type of Object. What is an Object?

If you're familiar with Python dictionaries, JavaScript Objects should be pretty simple; they are also lists of key-value pairs. Here's an example:

    var info = {
        name: "Ty",
        email: "me@example.com",
        age: 19
    };
    
We can then access the information in the object like this:

    console.log(info.name);
    
    >>> Ty
    
    var email = info.email;
    console.log(email);
    
    >>> me@example.com
    
We can also update the values, or add new keys!

    info.name = "Bob";
    
    info.job = "Web Developer";
    
    console.log(info);
    
    >>> Object {name: "Bob", email: "me@example.com", age: 19, job: "Web Developer"}
    
Understanding objects is important, because that's all you get in JavaScript! There are no classes, only objects.

**Dot and Bracket notation**

You've already seen one way of accessing values in Objects:

    myObject.someProperty
    
That's called "dot" notation. There's another syntax that uses brackets instead, but leads to the same effect:

    myObject["someProperty"]
    
I generally prefer the dot notation, but bracket notation is more common in other languages like Python.