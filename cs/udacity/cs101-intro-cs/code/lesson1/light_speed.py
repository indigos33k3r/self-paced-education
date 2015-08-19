# Write Python code to print out how far light travels 
# in centimeters in one nanosecond.  Use the values
# defined below.

# Note: Python (and most languages) will truncate rather than round
# if integers are used with division. Ex/ 2/5 = 0, but 2.0/5 = 0.4

# speed_of_light = 299792458   meters per second
# centimeters = 100            one meter is 100 centimeters
# nanosecond = 1.0/1000000000  one billionth of a second

# solution
print (1.0/1000000000) * 100 * 299792458


# Now let's use variables!

# Given the variables defined here, write Python 
# code that prints out the distance, in meters, 
# that light travels in one processor cycle. 

speed_of_light = 299792458.0
cycles_per_second = 2700000000.0

# solution
print speed_of_light / cycles_per_second

# we can change the value of a variable too
cycles_per_second = 2800000000.0

# meaning this will change
print speed_of_light / cycles_per_second