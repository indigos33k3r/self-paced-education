# JavaScript Basics

**Udacity: UD 804**

---

### Résumé overview

Udacity has already provided some code to get you started; let's go over it. Here's the project structure:

    js-resume/
        css/
            style.css
        images/
            179x148.jpg
            fry.jpg
        index.html
        js/
            helper.js
            jQuery.js
            resumeBuilder.js
        README.md
        
### HTML

If you aren't familiar with HTML, check out my notes from Udacity's Web Development class [here](https://github.com/tylucaskelley/courses/blob/master/udacity/cs253-web-development/notes/lesson1/2-html.md). That should tell you all you need to know about how HTML works.

Anyway, the HTML of our résumé, which is located in the `code/lesson1/js-resume` directory, looks like this (with comments removed):

    <!DOCTYPE html>
    <html>
        <head>
            <link href="css/style.css" rel="stylesheet" type="text/css"></link>
            <script src="js/jQuery.js"></script>
            <script src="js/helper.js"></script>
            <meta name="viewport" content="width=device-width">
        </head>
        <body unresolved>
            <div id="main">
                <div id="header" class="center-content">
                    <ul id="topContacts" class='flex-box'></ul>
                </div>
                <div style='clear: both;'></div>
                <div id="workExperience" class='gray'>
                    <h2>Work Experience</h2>
                </div>
                <div id="projects">
                    <h2>Projects</h2>
                </div>
                <div id="education" class='gray'>
                    <h2>Education</h2>
                </div>
                <div id="skillsChart">
                    <h2>Skills Chart</h2>
                </div>
                <div id="mapDiv">
                    <h2>Where I've Lived and Worked</h2>
                </div>
                <div id="letsConnect" class='dark-gray'>
                    <h2 class='orange center-text'>Let's Connect</h2>
                    <ul id="footerContacts" class="flex-box"></ul>
                </div>
            </div>
            <script src="js/resumeBuilder.js"></script>
            <script type="text/javascript">

                if(document.getElementsByClassName("flex-item").length === 0) {
                    document.getElementById("topContacts").style.display = "none";
                }

                if(document.getElementsByTagName("h1").length === 0) {
                    document.getElementById("header").style.display = "none";
                }

                if(document.getElementsByClassName("work-entry").length === 0) {
                    document.getElementById("workExperience").style.display = "none";
                }

                if(document.getElementsByClassName("project-entry").length === 0) {
                    document.getElementById("projects").style.display = "none";
                }

                if(document.getElementsByClassName("education-entry").length === 0) {
                    document.getElementById("education").style.display = "none";
                }

                if(document.getElementsByClassName("skills-entry").length === 0) {
                    document.getElementById("skillsChart").style.display = "none";
                }

                if(document.getElementsByClassName("flex-item").length === 0) {
                    document.getElementById("letsConnect").style.display = "none";
                }

                if(document.getElementById("map") == undefined) {
                    document.getElementById("mapDiv").style.display = "none";
                }
            </script>
        </body>
    </html>
    
### CSS

The project has some pre-defined stylesheets as well; if you're unfamiliar with CSS, check out CSS tutorials [here](http://docs.webplatform.org/wiki/css). Here's an example from `code/lesson1/js-resume/css/style.css`:

    .date-text {
        font-style: italic;
        font-size: 14px;
        color: #999999;
        line-height: 16px;
        float: left;
    }
    
### JavaScript
    
Most of the HTML and CSS is pretty basic; hopefully you've seen something like it before. What's of interest to us is the JavaScript. At the top of the file, we include a few JavaScript files:

    <script src="js/jQuery.js"></script>
    <script src="js/helper.js"></script>
    ...
    <script src="js/resumeBuilder.js"></script>
    
The first of these two files is [jQuery](http://jquery.com/), which is a JavaScript library so ubiquitous at this point that it's impossible to mention JavaScript without it. You won't be learning all about jQuery in this class, but you'll be exposed to it.

There's also `helper.js `, which is some code that Udacity has pre-written for us. Later down the page, there are some pre-written JavaScript statements that look like this:

    if(document.getElementById("map") == undefined) {
        document.getElementById("mapDiv").style.display = "none";
    }
    
These statements just check for the existence of some elements on the page, and hide certain `div` elements if needed. And finally, we load the file that we will be working in, `resumeBuilder.js`.

