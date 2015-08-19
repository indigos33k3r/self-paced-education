# Define a variable, name, and assign to it a string that is your name.
name = 'Ty'

# concatenation
full_name = name + ' Kelley'
print full_name

# multiplication
print name * 5
#TyTyTyTyTy

# indexing

rob = "Robert"

print rob[0]
#R

print rob[-1]
#t

print rob[0:3]
#Rob

print rob[:3]
#Rob

# Write Python code that prints out Udacity (with a capital U), 
# given the definition of s below.
s = 'audacity'
   
print "U" + s[2:]

# finding substrings
search_string = "I am a happy man, I promise I really am."
target_string = "am"
	
print search_string.find(target_string)
#2

#find with position parameter
search_string = "I am a happy man, I promise I really am."
target_string = "am"
	
print search_string.find(target_string, 10)
#37