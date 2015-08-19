# Object-Oriented JavaScript

**Udacity: UD 015**

---

### Prototype chains

Prototype chains are a mechanism for making objects that resemble other objects. Let's start by building some objects that have a similar structure, so we can see how prototype chains could help:

    var gold = {
        a:1
    };
    
    console.log(gold.a); //this works and logs 1
    
What happens if we try to access a property that `gold` doesn't have?

    console.log(gold.z);
    
    //undefined
    
The lookup for `z` on the `gold` object fails, and returns `undefined`. In other languages, you might get an error instead.

