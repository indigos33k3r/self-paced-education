# Object-Oriented JavaScript

**Udacity: UD 015**

---

### Lesson 2: The 'this' keyword

Most object-oriented languages use the keyword "this" for one reason or another. Usually, it's a reference to an instance of a class. However, `this` is different in JavaScript, and is one of the most misunderstood aspects of the language.

`this` is a parameter, just like any other one you've seen before that gets passed as input to a function. It has a few key differences that we will cover though. 

**What is 'this'?**

`this` is an identifier that gets a value bound to it automatically. The rules that determine what value `this` gets are similar to the rules for function scoping. Let's start with a simple function:

    var fn = function(a, b) {
        console.log(this);
    };

Here are some misconceptions people normally have about what `this` is bound to:

* the function object that it was referenced inside of
* an instance of that function is created and `this` is a reference to it
* an object that happens to have the function as a property
* an execution context defined at the time the function it's inside of is called

Instead, `this` refers to the object that the function is called from at execution time. Here's an example:

    var obj = {
        fn: function() {
            console.log(this);    
        }
    };
    
    obj.fn(); //"this" refers to "obj"
    
Calling `obj.fn` would print out the Object `obj`. Try it in the developer tools of your browser, or in the Node interpreter!
    
**Predicting 'this' output**

Let's create another function:

    var fn = function(a, b) {
        console.log(this, a, b);
    };
    
    fn(1, 2);
    
What will the output be? We already know that `a` and `b` will be assigned to 1 and 2, but what about `this`? We called the function from the global scope, not as the property of any other object like before, so it's not so obvious.

The answer is the global scope, also known as the global object. This is essentially the default object for whenever we don't have our own binding for the `this` keyword. See this for yourself by opening up a JavaScript interpreter (either Node or the dev tools), and typing "this". You'll get a massive object, which is the global object.

You can prove that `this` defaults to the global object by defining a variable in the global scope (let's use `var a = 1;`). Once you do that, you can get the value of `a` by typing `a` or `this.a`.

**Overriding 'this'**

We can override the default `this` value by using the `call` function that is a property of every function. Look here:

    var fn = function(a, b) {
        console.log(this, a, b);
    };
    
    fn(1, 2);
    
    //<global>, 1, 2
    
    var myObj = {
        name: 'bob',
        age: 12
    };
    
    fn.call(myObj, a, b);
    
    //{ name: 'bob', age: 12 }, 1, 2
    
Whenever you call a function using that `call` function, you get to pass in an extra parameter to define what `this` is bound to.