# JavaScript Syntax

**Udacity: UD 804**

---

### Lesson 3: Control Flow

At this point, we're pretty good at storing, accessing, and modifying data using JS. In addition, we've learned a bit about interacting with the DOM, and using the jQuery library to make things easier. Now, it's time to learn more about control flow in JavaScript.

If you're familiar with any other programming language, this should all be pretty similar:

**Comparison operators**

JavaScript has many comparison operators we can use to compare data. The output of a comparison is always `true`, `false`, or an error if you messed up.

* `<` less than
* `<=` less than or equal to
* `>` greater than
* `>=` greater than or equal to
* `==` loose equality
* `!=` loose not equals
* `===` strict equality
* `!==` strict not equals

Before I show you some examples, let me explain this "strict" and "loose" business. The `==` and `!=` operators are "loose", which means that they try to convert operands if they aren't of the same type. This goes back to the idea of "truthy" and "falsy" we talked about before. Here are some examples:

    0 == "0" //true
    0 == false //true
    1 == true //true
    "0" == true //false
    
However, it is generally best practice to NOT use the `==` if possible, and instead use the stricter `===` and `!==`:

    0 === "0" //false
    1 !== "1" //true
    1 === 1 //true
    "s" === 's' //true

Here are examples of the other operators in action:

    0 < 1 //true
    "s" < "e" //false

**If statements**

If statements help us make decisions, depending on a condition. They work in this way:

    //not actual code
    
    if (condition is true) {
        do this
    } else {
        do this instead
    }
    
We can also look for some other conditions by using the `else if` syntax:

    if (condition1) {
        //stuff
    } else if (condition2) {
        //stuff
    } else {
        //stuff
    }

You can have as many `else-if`'s as you want. Let's see this in practice:

    var x = 24;
    
    if (x % 2 == 0) {
        console.log("it is even!");
    } else {
        console.log("it is odd!");
    }
    
**While loops**

While loops execute until their condition is false. Not much needs to be said, so here's an example:
    
    var x = 0;
    
    while (x < 10) {
        console.log(x);
        x++;
    }

Be careful of infinite loops! This is legal syntax but will make your code run until your PC runs out of memory:

    while (true) {
        //oops
    }
    
Stick that in your dev console for a good time.

**For loops**

For loops are also pretty simple. They are in this form:

    for (initialization; condition; increment) {
        //do stuff
    }

For example:

    for (var i = 0; i < 10; i++) {
        console.log(i + ': ' + i * 10);
    }

**For-in loops**

This is a nice variation on the for loop that works well with arrays (since they have a length):

    var a = ['a', 'b', 'c', 'd', 'e', 'f'];
    
    for (var x in a) {
        console.log(a[x]);
    }