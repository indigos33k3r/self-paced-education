# JavaScript Basics

**Udacity: UD 804**

---

### Using documentation

Let's take this problem: turn the string "audacity" into "Udacity" using JavaScript.

There are many ways to go about the problem, and for a beginner, it's easy to get lost figuring out the best solution (or any solution). This is where being able to use documentation and the internet comes in handy! Here are some resources you should always turn to if you get stuck:

1. [Stack Overflow](http://stackoverflow.com): Q&A for programmers; be careful though, as not all answers are good answers. Look for ones with a lot of upvotes!
2. [Mozilla Developer Network](https://developer.mozilla.org/en-US/): An awesome site that has information about JavaScript everywhere. This is a huge site, but everything on there is very high quality.
3. [jQuery API Docs](http://api.jquery.com): The official documentation for the jQuery library; turn to this when you have jQuery questions becuase the information is up-to-date and the examples are great!

### Solving a problem

With that being said, let's solve the problem togehter! I'm going to go through three possible ways to change "audacity" into "Udacity".

1. `toUpperCase` and `slice`

        var s = "audacity";
        s = s[1].toUpperCase + s.slice(2);

2. `slice` and `replace`

        var s = "audacity";
        s = s.slice(1).replace("u", "U");
        
3. Brute force

        var s = "audacity";
        s = "Udacity";
        
For the problem at hand, all of these solutions are valid! When we learn about functions later on, we will focus more on generating solutions that can handle more than one specific input.