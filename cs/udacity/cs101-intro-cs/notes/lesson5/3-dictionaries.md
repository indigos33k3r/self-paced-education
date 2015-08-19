#Intro to Computer Science

**Udacity: CS 101**

---

###Dictionaries

Now that we know how hash tables work, and have implemented a basic one ourselves, it's time to introduce a Python data structure that can make things easier for us: the *dictionary*.

Unlike a list or string, which are sequences, a dictionary is a mapping of keys to values. They look like this:

	elements = {
		'hydrogen': 1,
		'helium': 23
	}
	
Just like with a hash table, we can look up a key and get its value in constant time. Just like lists, dictionaries are mutable; we can change the value of any key. Accessing values is where dictionaries differ from strings and lists:

	my_string = "hello"
	my_list = [10, 100, 1000, 10000, 100000]
	my_dict = {
		'greeting': 'hello',
		'age': 23
	}
	
	print my_string[0]
	
	>>> h
	
	print my_list[0]
	
	>>> 10
	
	print my_dict['greeting']
	
	>>> hello
	
Pretty simple, but different from what we are used to. Let's demonstrate the mutability of dictionaries:

	my_dict = {
		'a': 0,
		'b': 1
	}
	
	print my_dict['a']
	
	>>> 0
	
	my_dict['a'] = 5
	
	print my_dict['a']
	
	>>> 5
	
Also, just like lists, we can nest dictionaries inside one another. This next example should demonstrate the organizational power of dictionaries:

	students = {
		'Bob Johnson': {
			'id': 15246,
			'age': 15,
			'gpa': 4.0
		},
		'Sam Robinson': {
			'id': 11213,
			'age': 14,
			'gpa': 3.5
		}	
	}
	
	def add_student(name, info):
		if name not in students:
			students[name] = info
	
	def update_gpa(name, new_gpa):
		if name in students:
			students[name]['gap'] = new_gpa
			

These procedures allow us to add and edit the information of new students into the `students` dictionary very easily. Let's see them in use:

	joe = {
		'id': 44444,
		'age': 15,
		'gpa': 3.78
	}
	
	add_student('Joe Robertson', joe)
	
	print students['Joe Robertson']['gpa']
	
	>>> 3.78
	
	update_gpa('Joe Robertson', 2.8)
	
	print students['Joe Robertson']['gpa']
	
	>>> 2.8

	
Hopefully, you can appreciate how much easier dictionaries will make our job! So, what happens if we try to access a key in a dictionary that doesn't exist? A `KeyError`:

	stuff = {
		'a': 0,
		'b': 1,
		'c': 2
	}
	
	print stuff['d']
	
	>>> Traceback (most recent call last):
			File "<stdin>", line 1, in <module>
		KeyError: 'd'
	
That doesn't mean we couldn't make that new key on the fly though:

	stuff['d'] = 3
	
	print stuff['d']
	
	>>> 3
	
Easy as that! What if we don't want to get errors when we try to access a key that doesn't yet exist? There are several ways:

Strategy one uses the popular ["EAFP"](https://docs.python.org/2/glossary.html#term-eafp) philosophy, which says that it's easier to ask for forgiveness than permission:

	def get_value(dict, key):
		try:
			return dict[key]
		except KeyError:
			return None
			
Strategy 2 uses the also popular ["LBYL"](http://python.net/~goodger/projects/pycon/2007/idiomatic/handout.html#eafp-vs-lbyl) form of programming, which suggests that you look before you leap:

	def get_value(dict, key):
		if key in dict:
			return dict[key]
		return None
		
Now that we know about dictionaries, it's time to modify the search engine to take advantage of them! We will have to modify `crawl_web`, `add_to_index`, and `lookup` to stop using lists:

	def crawl_web(seed):
    to_crawl = [seed]
    crawled = []
    index = {}
    while to_crawl:
        page = to_crawl.pop()
        if page not in crawled:
            content = get_page(page)
            add_page_to_index(index, page, content)
            union(to_crawl, get_all_links(content))
            crawled.append(page)
    return index
    
    def lookup(index, keyword):
    if keyword in index:
        return index[keyword]
    return None

	def add_to_index(index,keyword,url):
    		if keyword in index:
        		index[keyword].append(url)
    		else:
        		index[keyword] = [url]

We are now done with our basic search engine! We could definitely make improvements. Let's start by figuring out a way to rank pages, to return the best results, rather than all of the results. See you in Lesson 6!