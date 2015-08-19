# Define a procedure, product_list,
# takes as input a list of numbers,
# and returns a number that is
# the result of multiplying all
# those numbers together.

def product_list(nums):
    return reduce(lambda x, y: x * y, nums) if nums else 1
    
print product_list([9])
#>>> 9

print product_list([1,2,3,4])
#>>> 24

print product_list([])
#>>> 1

# alternative solution

def for_product_list(nums):
    product = 1
    for item in nums:
        product *= item
    return product