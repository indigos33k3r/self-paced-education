#Programming Foundations with Python

**Udacity: UD036**

---

###Working with Files

Let's say you have a bunch of photos in a folder on your computer (for this section, I'd recommend getting a folder full of photos to match what I'll write below). The photos are nice, but they have a bunch of numbers in the filenames, making them hard to read:

	photos/
		12tokyo.png
		new4york.png
		paris3.png
		
In this case, three photos is pretty manageable, and we could rename them one by one. But, what if there were 100 photos? Let's write a program that can strip out all of the numbers from these filenames.

Here's one way to go about solving the problem:

1. Read all of the filenames from a folder
2. Strip out the numbers from those filenames
3. Write the new names back into the files

To do this, we're going to need to learn how to read and write to files in Python. A quick Google search will tell us about a module called `os`.

`os` lets us work with the operating system's filesystem, among many other things. The first function we need is something called `listdir`, which will, as the name suggests, list all of the files in a directory. Let's put it to use:

	import os
	
	path = 'img' #path to your folder of pictures
	
	files = os.listdir(path)
	
	print files
	
	>>> ['12tokyo.jpg', 'new4york.jpg', 'paris3.jpg']
	
Nice! We've already got the files that we need, with only one function. Now, we need to *iterate* over that list of files and operate on them. Let's continue our program:

	import os
	
	path = 'img'
	files = os.listdir(path)
	
	for f in files:
		# do something
		
As far as the "do something" is concerned, we need to rename those files. `os` provides another function we can use to achieve this goal, called `rename`. This function takes in two arguments, the original name and the new name:

	import os
	path = 'img'
	files = os.listdir(path)
	
	for f in files:
		rename(f, strip_nums(f))
		
Notice how I passed in `strip_nums(f)`? That's because we're going to leave the actual renaming part to a separate procedure we will write. We can do this with a simple list comprehension:

	def strip_nums(s):
		return ''.join([c for c in s if not c.isdigit()])
		
For those of you who aren't used to list comprehensions, check out [this]() tutorial. This procedure simply returns a string generated from the characters in the original string that *aren't digits*. So, "paris123" would become "paris". Just what we needed!

Let's put it all together:

	import os
	path = 'img'
	files = os.listdir(path)
	
	def strip_nums(s):
		return ''.join([c for c in s if not c.isdigit()])
	
	for f in files:
		rename(f, strip_nums(f))

###A Small Bug
		
Looks good, right? Let's run it:

	>>> Traceback (most recent call last):
			File "rename.py", line 10, in <module>
				os.rename(str(f), strip_nums(f))
			OSError: [Errno 2] No such file or directory
			
Hmm, the error is telling us that it can't find the file specified. This is because although we were able to grab all those filenames, we aren't actually working in that directory when trying to rename them. To fix this, we can use a command called `os.chdir` to move to the correct folder, where the images are:

	import os
	
	path = 'img'
	files = os.listdir(path)
	
	os.chdir(path) # move to images folder before working in it
	
	def strip_nums(s):
		return ''.join([c for c in s if not c.isdigit()])
	
	for f in files:
		rename(f, strip_nums(f))
		
Looking at the files in our images folder proves that it worked: all the numbers are gone! We successfully wrote a program to change filenames on our operating system, and learned a little in the process:

1. How to use the `os` module
2. How to debug when something goes wrong

###Mini-Project

Let's make our program a bit more useful. How about we do two things:

1. Let the user pick a directory to look for files in
2. Let the user decide what to strip from the files (instead of just numbers)

Can you figure it out? If not, here's my solution:

	import os, sys

	path = sys.argv[1] if len(sys.argv) > 1 and os.path.isdir(sys.argv[1]) else 'img'
	chars_to_strip = sys.argv[2] if len(sys.argv) > 2 else "0123456789"
	files = os.listdir(path)

	def strip(s):
		return ''.join([c for c in s if not c in chars_to_strip])

	os.chdir(path)

	for f in files:
		os.rename(f, strip(f))
		
Notice how I take some precaution by providing default values in case the user didn't input anything, or if the input they gave was invalid. Time to move on!