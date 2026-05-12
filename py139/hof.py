# problem 1
# The three conditions an object must satisfy to be considered a first class citizen in Python are the following:
# 1. The object can be assigned to a variable or stored in another object, like a dictionary or a list
# 2. The object can be passed into a function as an argument
# 3. the object can be returned from a function as a return value

# problem 2
# A first class function is a description of what kind of object a function is. In this case, it's a function that satisfies all the requirements of a first-class object
# In Python, all functions are first-class functions.

# problem 3
# A higher order function is a function that does at least one of the following:
# it expects one or more functions as an argument
# it returns a function as a return value

# problem 4
# `sorted(my_list, key=len))` can be considered a higher-order function, since it takes the `len()` function as an argument. The keyword argument, key, expects a function.
# Thus, it satisfies one of the criteria required for a higher-order function, namely that it expects a function as an argumnet

# problem 5
def say_hello(name):
    print(f"Hello, {name}!")

def say_goodbye(name):
    print(f"Goodbye, {name}!")

def operate(action, name):
    action(name)

operate(say_hello, "Alice") # outputs Hello Alice!
operate(say_goodbye, "Bob") # outputs Goodbye Bob!
# here, `action` is a parameter in the higher-order function `operate()` that accepts a first-class function as an argument
# In this case, the first-class function, in this context, also a callback function, is `say_hello()` or `say_goodbye()`
# We can identify `operate()` as a higher-order function since it expects a function as an argument.
# We can identify the functions say_hello() and `say_goodbye()` as first-class functions since they can be passed into `operate()` as arguments.

# problem 6
# Essentially, all Python functions are first-class functions, but only some are higher-order functions
# The first-class descriptor is a fundamental property of all​ functions in Python. It means they can be passed around and manipulated just like any other data type.
# A higher-order function is just a specific ​type​ of function that either expects one or mor functions as an argument or returns a function.
# Given that a higher-order function either returns a value or expects functions as an argument, it would be impossible for a language to support higher-order functions without also supporting first-class functions.

# problem 7
def apply_to_all(lst, func):
    return [func(item) for item in lst]

def squared(num):
    return num ** 2

numbers = [1, 2, 3, 4]
print(apply_to_all(numbers, squared))

# problem 8
def create_adder(x):
    def adder(y):
        return x + y
    return adder

add_five = create_adder(5)
add_ten = create_adder(10)

print(add_five(3)) # outputs 8
print(add_ten(3)) # output 13
print(add_five(10)) # outputs 15

# Here, `create_adder` is using a closure to perform a programming technique known as partial function application (PFA)
# This technique fixes certain arguments in a function, so as to make functions with less arguments.
# Thus, here, `create_adder()` is generating and returning functions of lower arity, with the argument passed into `create_adder()` as the fixed value
# In this case, the function assigned to the variable `add_five`, which is the return value of the `create_adder(5)` function, is fixed with the integer 5
# A similar situation occurs for the function assigned to the variable `add_ten`, which has been fixed with the integer 10.
# Thus, when calling those functions with an argument through the variables, we can perform more constrained applications of the original function.

# problem 9
people = [
            {'name': 'Alice', 'age': 25, 'city': 'New York'},
            {'name': 'Bob', 'age': 30, 'city': 'London'},
            {'name': 'Charlie', 'age': 25, 'city': 'New York'},
        ]

def find_matching(lst, predicate):
    return [person for person in lst if predicate(person)]


def find_new_yorkers(item):
    return item['city'] == 'New York'


def find_older_than_twenty_five(item):
    return item['age'] > 25

print(find_matching(people, find_new_yorkers))
print(find_matching(people, find_older_than_twenty_five))

# problem 10
def create_general_repeater(action_word):
    def nested(n, obj):
        method = getattr(obj, action_word)
        for _ in range(n):
            method()



    return nested

bark_repeater = create_general_repeater('bark')
drive_repeater = create_general_repeater('drive')

class Dog:
    def bark(self):
        print('bark!')

class Car:
    def drive(self):
        print('vroom!')

fluffy = Dog()
tom = Car()

bark_repeater(5, fluffy)
drive_repeater(5, tom)
