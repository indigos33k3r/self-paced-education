# JavaScript Basics

**Udacity: UD 804**

---

### Arrays

In JavaScript, arrays are just lists of values. Anyone familiar with Python should feel at home here, because arrays can hold values of any type! Check it out:

    var myArray = [22, "hello", false];
    
Pretty simple! Just like in any other language, JS arrays are indexed so we can easily access items:

    var b = myArray[2];
    
    console.log(b);
    
    >>> false
    
Just like in most languages, arrays are zero-indexed, meaning that 0 is the index of the first value.

We can also reassign values in the array:

    myArray[0] = 1;
    
    console.log(myArray);
    
    >>> [1, "hello", false]

**Length**

Arrays also have some properties associated with them. Length is one:

    var n = myArray.length;
    console.log(n);
    
    >>> 3
    
To learn more about arrays, check out the docs on [MDN](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array). Using just what we know, we can grab the last element of any array:

    var a = ["hello", 22, false, 3];
    
    //time to get the last element
    
    console.log(a[a.length - 1]);
    
    >>> 3
    
**Push and Pop**

So far, all we've done with arrays is declare them, change the values of a few elements, and use the `length` function. What about adding and deleting?

`push` and `pop` allow us to use JavaScript arrays as a [stack](http://www.cs.cmu.edu/~adamchik/15-121/lectures/Stacks%20and%20Queues/Stacks%20and%20Queues.html), so we can add and remove elements at the end of the array.

Here's the functions in action:

    var a = [0, 1, 2];
    
    var lastElement = a.pop(); //removes and returns the last element of a
    console.log(lastElement);
    
    >>> 2
    
    console.log(a);
    
    >>> [0, 1]
    
    a.push("hello");
    console.log(a);
    
    >>> [0, 1, "hello"]