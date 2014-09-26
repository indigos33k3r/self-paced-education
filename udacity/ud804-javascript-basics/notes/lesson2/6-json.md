# JavaScript Basics

**Udacity: UD 804**

---

### JSON

**What is JSON?**

JavaScript Object Notation. JSON is a popular and simple format for storing and transferring nested or hierarchal data. It's so popular that most other programming languages have libraries capable of parsing and writing JSON (like [Python's JSON library). ](https://docs.python.org/2/library/json.html) Internet GET and POST requests frequently pass data in JSON format. JSON allows for objects (or data of other types) to be easily encapsulated within other objects. See the [MDN](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/JSON) or [JSON.org ](http://json.org/) for more details.

[This](http://www.copterlabs.com/blog/json-what-it-is-how-it-works-how-to-use-it/) is a fantastic deep dive from Jason Lengstorf about JSON and its ubiquitous use in the form of AJAX requests.

**Example**

Here's what some valid JSON looks like:

    {
        "schools": [
            {
                "name": "University of California",
                "major": "Computer Science",
                "degree": "BS",
                "gpa": 4.0
            },
            {
                "name": "MIT",
                "major": "Computer Science",
                "degree": "MS",
                "gpa": 3.78
            }
        ],
        "foods": [
            "bananna", "apple", "orange"
        ]
    }

**Why should I lint my JSON?**

With a mix of nested curly braces, square brackets and commas, it's easy to make mistakes with JSON. And mistakes mean bugs.

If you're generating JSON by hand, you should copy and paste your code into a JSON linter like [jsonlint.com](http://jsonlint.com/) to quickly and easily find syntax errors. A linter is a piece of software that analyzes code for syntax errors. Some text editors, like Sublime Text, will automatically lint (or highlight) most syntax errors. But a JSON linter won't miss any syntax errors and you can rest assured that your JSONs will be properly formatted.