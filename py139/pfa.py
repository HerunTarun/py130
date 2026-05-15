from functools import partial
# problem 1
# partial function application is a programming technique that involves fixing a number of arguments to a function, which then produces a function of smaller arity.
# In essence, a partially applied function is a version of the original function with some arguments already set
# This would be particularly useful if you have a general function, let's say a function that takes a base and an exponent.
# If you wanted to make functions that only used the integer 2 as a base, then you could use partial function application on your general function to generate a specific function that always used 2 as a base

# problem 2
def calculate_price(tax_rate, base, discount):
    return base * (1 + tax_rate) * (1 - discount)

calculate_ca_price = partial(calculate_price, .0825)

print(calculate_ca_price(100, .1))

# problem 3
def display_config(user, color, font_size, theme='light'):
    print(f"User: {user}")
    print(f"Color: {color}")
    print(f"Font Size: {font_size}px")
    print(f"Theme: {theme}")

user_prefs = partial(display_config, 'admin', font_size=16)
user_prefs(color='blue', theme='dark')
# User: admin
# Color: blue
# Font Size: 16px
# Theme: dark
# Here, we've used the partial function from the functools module to perform partial function application,
# where we've fixed the value of user positionally to the value 'admin', and the value of font_size using keyword to the value 16
# then, when we call the return value of the partial function call, which is a function assigned to the variable user_prefs,
# we pass in the arguments through the keywords color and theme
# Since all the arguments have been either fixed or passed in, the function successfully executes all the print statements

# problem 4
def create_partial(func, *args):
    def fixed_func(*more_args, **kwargs):
        func(*args, *more_args, **kwargs)

    return fixed_func

# problem 5
# LSBot asked about currying, which is not covered, so skipped

# problem 6
def power(base, exponent):
    return base ** exponent

square = partial(power, exponent=2)

# What does this print?
print(square(3)) # 9

# What about this?
print(square(3, exponent=3))
# leave for later, LSBot made a boo boo

# problem 7
products = [
        {'name': 'Laptop', 'price': 1200, 'rating': 4.5, 'stock': 32},
        {'name': 'Mouse', 'price': 25, 'rating': 4.8, 'stock': 150},
        {'name': 'Keyboard', 'price': 75, 'rating': 4.2, 'stock': 88},
    ]
def price_sorting(item):
    return item['price']

sort_by_price = partial(sorted, key=price_sorting)
print(sort_by_price(products))

# problem 8
def my_partial(func, *args, **kwargs):
    def partial_func(*more_args, **more_kwargs):
        final_kwargs = kwargs.copy()
        final_kwargs.update(more_kwargs)
        func(*args, *more_args, **final_kwargs)
    return partial_func
# problem 9

# problem 10
