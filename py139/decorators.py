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
# Applying Decorator One
# Wrapper One: Before call
# Wrapper One: After call
# Applying Decorator Two
# Wrapper Two: Before Call
# Wrapper Two: After Call

# problem 9

# problem 10
