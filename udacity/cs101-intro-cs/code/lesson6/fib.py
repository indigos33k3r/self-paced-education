import time

def watch(func):
    start = time.clock()
    eval(func)
    runtime = time.clock() - start
    return runtime

def recursive_fib(n):
    return n if n < 2 else recursive_fib(n-1) + recursive_fib(n-2)

def iterative_fib(n):
        a, b = 0, 1
        for i in range(0,n):
            a, b = a + b, a
        return a

print "Iterative:"
print watch('iterative_fib(0)')
print watch('iterative_fib(5)')
print watch('iterative_fib(10)')
print watch('iterative_fib(15)')
print watch('iterative_fib(20)')
    
print "Recursive:"
print watch('recursive_fib(0)')
print watch('recursive_fib(10)')
print watch('recursive_fib(20)')
print watch('recursive_fib(30)')
print watch('recursive_fib(40)')
