# Web Development

**Udacity: CS 253**

## Lesson 2A: Templates w/ Jinja

Templates are a way of building complicated strings. The library built in to Google App Engine is called "jinja2". They make things easier compared to hard coding HTML strings into Python files.

####Variable Substitution (in jinja)

{{ variable }}

####Statement Syntax

Despite the fact that whitespace is used in Python to mark the ends of statements and definitions, Jinja statements are formed like this:

{% statement %}
	output
{% end statement %}

* ex/ if statement:

		{% if name == "steve" %}
			Hello, Steve
		{% else %}
			Who are you?
		{% endif %}
		
####For loop syntax

{% for statement %}
	body
{% endfor %}

####Tips and Tricks

* **ALWAYS AUTMOATICALLY ESCAPE VARIABLES WHEN POSSIBLE IN A TEMPLATING LANGUAGE**
* Minimize the amount of HTML in code

####Template Inheritance

Since there will always be repetition in HTML, one template can include re-used things like headers and footers, while *sub-templates* will take care of the content.

(For example, see ./app-engine/shopping files)

