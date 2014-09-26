# JavaScript Syntax

**Udacity: UD 804**

---

### Functions

Functions are the last thing we will learn about in this course, and the most important! In JavaScript, functions can be defined in two ways. They are both equivalent (well, [mostly](http://stackoverflow.com/questions/9423693/javascript-function-definition-syntax)):

    //first way
    var add = function(a, b) {
        return a + b;
    };
    
    //second way
    function add(a, b) {
        return a + b;
    }
    
Just like any other language, the `return` statement is the output of the function. We could then call our `add` function like this:

    var x = 1, y = 2; //multiple assignment, just like python
    
    var sum = add(x, y);
    
    console.log(sum);
    
    >>> 3

**Encapsulation**

Functions are objects too!
    
Something that's cool about JavaScript is that we can pass functions to other functions. This is because functions are "first-class objects"; this means that we treat them like any old variable. Read more [here](http://helephant.com/2008/08/19/functions-are-first-class-objects-in-javascript/), and take a look at this example:

    function runner(fn, args) {
        fn(args);
    }
    
    var printer = function(arr) {
        for (var i in arr) {
            console.log(arr[i]);
        }
    }
    
    x = [0,1,2,3,4,5];
    runner(printer, x);
    
Pretty cool! We can go further with this:

    var me = {
        name: "Ty",
        age: 19,
        sayHello: function(person) {
            console.log("Hello, " + person + "!");
        }
    };
    
    me.sayHello('Barack Obama');
    
    >>> Hello, Barack Obama!
    
**Anonymous functions**

This is another cool piece of JavaScript. Functions can take other functions as arguments, but we don't even need to define those functions first! Take a look at this:

    $(document).click(function(loc) {
        console.log(loc.pageX, loc.pageY);
    });
    
Anonymous functions are functions that don't have a name and are often returned by other functions and objects. 

Some JavaScript libraries ask for a callback function to be executed once they have have the results of a task. Anonymous functions are used in these cases because there is not a need to call the function by name outside the confines of the enclosing function.

For example, in the code below which reads a JSON file from the server. After loading, it executes an anonymous function to print out the data.

    $.getJSON("test.json", function(data) {
        console.log(data);
    });

Anything that uses an anonymous function could also use a named function. The following code is also valid and is equivalent to what's listed above:

    var printData = function(data){ 
        console.log(data)
    };

Read more about [anonymous functions in JavaScript](http://en.wikipedia.org/wiki/Anonymous_function#JavaScript)! They are central to how the language works.