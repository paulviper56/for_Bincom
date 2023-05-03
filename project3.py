# A program to sum the first 50 fibonacci sequence
def fibonacci(n, my_cache=None):
    my_cache={}
    if n in my_cache:
        return my_cache[n]
    if n <= 1:

        return 1
    elif n == 2:
        return 1
    else:
        
        value = fibonacci(n-1,my_cache) + fibonacci(n-2,my_cache)
        my_cache[n] = value
        return value
for n in range(1,50):
    print(n, "-->", fibonacci(n))