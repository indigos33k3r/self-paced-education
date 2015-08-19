# Object-Oriented JavaScript

**Udacity: UD 015**

---

### Closures

Closures are a concept that many people find confusing. A closure is a function that refers to an "independent" variable. In other words, the function defined in the closure remembers the envorinment in which it was created.

Let's refactor our code from earlier, with the goal of keeping a reference to each of the `saga` function objects after the `newSaga` calls that created them returned. We could do this in several ways:

* passing the value to `setTimeout`
* returning `saga` from `newSaga`
* saving `saga` to the global scope

Let's start by making a global variable called `sagas` to store saga objects for access outside of the `newSaga` function:

    var sagas = [];
    var hero = aHero();
    
    var newSaga = function() {
        var foil = aFoil();
        sagas.push(function() { //we are adding a new function object to the sagas array
            var deed = aDeed();
            console.log(hero + deed + foil);
        }); //since there are no "()" after the anonymous function is defined, we aren't storing its result, just the function itself
    };
    
    newSaga();
    sagas[0]();
    sagas[0]();
    newSaga();

Now, what happens when we call `sagas[0]`? A new execution context is created, and believe it or not, it's inside of the `newSaga` context just like before. That's because the context for a function will always be created in the same context of the function it was defined inside of. This means that the function, although we defined it differently, still has access to the same variables as before.

When we run `sagas[0]` again, we will get a new `deed` value but the `foil` will remain the same. Just like before, again! However, when we call `newSaga` for the second time, the `sagas` array is going to get a new function object at index 1.

So, what will be the output of this then?

    newSaga();
    sagas[0]();
    sagas[0]();
    newSaga();
    sagas[0]();
    sagas[1]();
    
As we would hope, calling `sagas[0]`, even after we created a new context by calling `newSaga` again, will still use the same value for `foil` as before. It is only when we call `sagas[1]` that we get a new `foil`. No matter how many times we call `saga[0]`, it will keep using the same `foil`. Only the `deed` will continue to change with each call.