# problem 1
# A decorator is a function that accepts a function as an argument and returns a new function that wraps the original function argument, modifying the final behavior.
# A decorator would not be able to operate without functions being a first-class object, since it requires a function to be passed in as an argument, as well as returned as a return value
# It may also depend on the last criteria of a first-class object, that it can be assigned to a variable or stored in another object, as part of its wrapping logic

# problem 2
def emphasize(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return f"*** {result} ***"
    return wrapper

def get_greeting(name):
    return f"Hello, {name}!"

get_greetings = emphasize(get_greeting)

print(get_greetings('World'))

# problem 3
# It is generally considered best practice to use *args and **kwargs in the wrapper function of a decorator to ensure that we are flexible in the number of positional and keyword arguments the wrapped function accepts
# If we didn't, we would run into unexpected errors if our wrapped function accepted more or less arguments than listed in the wrapper function definition
# def emphasize(func):
#     def wrapper():
#         result = func()
#         return f"*** {result} ***"
#     return wrapper

# def get_greeting(name):
#     return f"Hello, {name}!"

# get_more_greetings = emphasize(get_greeting)

# print(get_more_greetings('World'))
# Here, we expect a kwarg argument when calling the wrapped function, but we don't pass one in, so Python raises a TypeError

# problem 4
# Closures are the mechanism by which we implement the wrapping of a function.
# In a standard decorator structure, like below, the closure is the wrapper function, which has access to the non-local variable func
def decorator(func):
    def wrapper(*args, **kwargs):
        pass # wrapper logic
    return wrapper

# problem 5
# talking about functools.wraps, so skip for now

# problem 6
def log_args(func):
    def wrapper(*args, **kwargs):
        print(f'Calling {func.__name__} with args: {args} and kwargs: {kwargs}')
        result = func(*args, **kwargs)
        return result
    return wrapper
@log_args
def add(x, y):
    """Adds two numbers."""
    return x + y

add(5, y=10)

# problem 7
def returns_type(type):
    def type_decorator(func):
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            if not isinstance(result, type):
                raise TypeError("Wrong type!")

            return result
        return wrapper

    return type_decorator
@returns_type(str)
def get_name(user_id):
    if user_id == 1:
        return "Alice"
    return 404 # Should raise a TypeError

@returns_type(int)
def get_id(name):
    return 1

print(get_name(1)) # Should return "Alice"
print(get_id("Bob")) # Should return 1
try:
    get_name(2) # Should raise TypeError
except TypeError as e:
    print(f'{e}')

# problem 8
def decorator_one(func):
    print("Applying Decorator One")
    def wrapper(*args, **kwargs):
        print("Wrapper One: Before call")
        result = func(*args, **kwargs)
        print("Wrapper One: After call")
        return result
    return wrapper

def decorator_two(func):
    print("Applying Decorator Two")
    def wrapper(*args, **kwargs):
        print("Wrapper Two: Before call")
        result = func(*args, **kwargs)
        print("Wrapper Two: After call")
        return result
    return wrapper

@decorator_one
@decorator_two
def calculate(a, b):
    print("Executing 'calculate'")
    return a + b

calculate(5, 3)
# The output would be:
# Applying Decorator Two
# Applying Decorator One
# Wrapper One: Before Call
# Wrapper Two: Before Call
# Executing 'calculate'
# Wrapper Two: After Call
# Wrapper One: After Call
# Here, we have two decorators stacked above the `calculate` function
# Decoration order is another term for the order in which decorators are applied. In this case, this is typically from bottom-to-top
# Thus, decorator_two is applied first, then decorates the function returned from that with decorator_one
# Invocation order is a term for the order in which Python calls decorators when it encounters them in code.
# The invocation order of a decorated function runs from top-to-bottom
# In this case, the function returned by decorator_one is called first, then the function returned by decorator_two, then calculate()

# problem 9
import time
# def memoize(func):
#     memoize_dict = {}
#     def wrapper(*args):
#         if args in memoize_dict.keys():
#             return memoize_dict[args]
#         result = func(*args)
#         memoize_dict[args] = result
#         return result
#     return wrapper

class Memoize:
    def __init__(self, func):
        self.func = func
        self.cache = {}

    def __call__(self, *args):
        if args in self.cache:
            return self.cache[args]

        result = self.func(*args)
        self.cache[args] = result
        return result

@Memoize
def slow_sum(a, b):
    print(f"Computing {a} + {b}...")
    time.sleep(1)
    return a + b

print(slow_sum(3, 4)) # Takes ~1 second, prints "Computing..."
print(slow_sum(3, 4)) # Returns immediately, does not print "Computing..."
print(slow_sum(5, 6)) # Takes ~1 second, prints "Computing..."
print(slow_sum(5, 6)) # Returns immediately, does not print "Computing..."
# problem 10

class CountCalls:
    def __init__(self, func):
        self.func = func
        self.calls = 0

    def __call__(self, *args, **kwargs):
        self.calls += 1
        return self.func(*args, **kwargs)

@CountCalls
def say_hello():
    print('Hello!')

say_hello()
say_hello()
print(say_hello.calls) # 2

@CountCalls
def say_goodbye():
    print('Goodbye!')

say_goodbye()
print(say_goodbye.calls) # 1
print(say_hello.calls) # 2
