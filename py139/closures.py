# problem 1
def create_power_func(exponent):
    def power(base):
        return base ** exponent
    return power

power_of_2 = create_power_func(2)
power_of_3 = create_power_func(3)

print(f"8 to the power of 2 is: {power_of_2(8)}") # 64
print(f"5 to the power of 3 is: {power_of_3(5)}") # 125
# Here, the programmer is employing partial function application, a technique that involves fixing a number of arguments to a function, which then produces a function of smaller arity.
# This technique is demonstrated here using closures.
# The invocation of create_power_func() creates and returns a function whose exponent argument is fixed
# Thus, the two functions that are created are assigned to the variables `power_of_3` and `power_of_2`
# These new functions are unrelated to each other, despite originating from the same function, because they come from two separate invocations of create_power_func()
# Thus, when we invoke the functions through their variables, passing in a base argument, in the print function, the function calculates and returns separate values to be printed to console.

# problem 2
multipliers = []
for i in range(3):
    multipliers.append(lambda x: x * i)

# Expected output:
# print(multipliers[0](10)) # 0
# print(multipliers[1](10)) # 10
# print(multipliers[2](10)) # 20

# Actual output:
print(multipliers[0](10))
print(multipliers[1](10))
print(multipliers[2](10))
# This is an example of late binding in lambdas.
# Specifically, the lambda captures a reference to the loop variable i inside the for loop when it is created and appended, not the actual value of the loop variable
# That evaluation only occurs when the lambda is called in the print statement
# At that point, the value of the loop variable is the value of the last iteration, 2
# Thus, the actual output is:
# 20
# 20
# 20
multipliers = []
for i in range(3):
    multipliers.append(lambda x, i=i: x * i)
# We fix late binding by forcing early binding within the loop.
# By giving i a default value, we force the lambda to capture the value of i upon definition, rather than when invoked.

# problem 3
def make_counter():
    counter = 0
    def number_of_calls():
        nonlocal counter
        counter += 1
        return counter

    return number_of_calls

# Example usage:
counter1 = make_counter()
print(counter1())  # Expected output: 1
print(counter1())  # Expected output: 2

counter2 = make_counter()
print(counter2())  # Expected output: 1
print(counter1())  # Expected output: 3


# problem 4
message = "Global"

def outer_func():
    message = "Outer"

    def inner_func():
        nonlocal message
        message = "Inner"
        return message

    return inner_func

my_func = outer_func()
print(my_func()) # Inner
print(message) # Global
# here we have an example of variable shadowing, as well as the reassignment of a free variable.
# the variable message, which has the string 'Outer' assigned to it, located inside outer_func() shadows the global variable message, which has the string 'Global' assigned to it
# however, inside inner_func, we use the nonlocal keyword to reassign the lexical scope message variable to the string 'Inner"
# When outer_func() is invoked, inner_func() is then assigned to the global variable my_func
# Thus, when we invoke my_func and print its return value, we see 'Inner', since that's the string assigned to message
# However, when we print message, we're referencing the global variable message, so we see 'Global'

# problem 5
def make_list_appender(lst):
    def append_to_list(value):
        lst.append(value)

    return append_to_list

# Example usage:
data = [1, 2, 3]
appender = make_list_appender(data)
appender(4)
appender(5)
print(data) # Expected output: [1, 2, 3, 4, 5]
# we see from the print statement that the function returned by make_list_appender(), append_to_list, does in fact mutate the original list, since we called it twice
# in order for a function to be a closure, it has to satisfy three criteria
# first, it has to be a nested function, which append_to_list is
# second, it has to close over a free variable. In this case, it's the local variable lst in its lexical scope
# third, it must be exposed, typically by being returned, which it is in this case.


# problem 6
# A free variable is a variable that is referenced within a closure, but not local to it nor in the global scope.
# Specifically, free variables are variables defined in the closure's lexical scope.
# These free variables are bound to the objects assigned to them when the closure was created.
def make_greeter(salutation, title):
    def greeter(name):
        return f"{salutation}, {title} {name}!"
    return greeter

greet_madam = make_greeter("Hello", "Madam")
print(greet_madam("Jones"))
# Here, we have two free variables, salutation, and title. They both exist in the lexical scope of greeter() and are referenced within the nested function.

# problem 7
val = 100

def func1():
    val = 1
    def func2():
        print(val)

    return func2

def func3():
    val = 2
    def func4():
        nonlocal val
        val = 3
        print(val)

    return func4

fn2 = func1()
fn4 = func3()

fn2() # 1
# Here, when we invoke fn2, we look at the return value of func1, which is func2
# In func2, we reference the free variable val, which is found in the lexical scope of func2
# there, val is assigned the value of 1, so the invocation of fn2 resolves to printing 1
fn4() # 3
# Here, when we invoke fn4, we look at the return value of func3, which is func4
# In func4, we reference the free variable val, which we reassign, using the nonlocal keyword, to the value 3
# thus, the invocation of fn4 resolves to printing 3
print(val) #100
# Here, the print invocation references the global variable val, which is assigned the value 100
# Thus, the print invocation resolves to printing 100

# problem 8
def password_protected_func(password, protected_function):
    def try_password(password_attempt):
        if password_attempt == password:
            return protected_function()
        return 'Invalid password'

    return try_password

def secret_action():
    return "The secret code is 1234."

access_secret = password_protected_func("password123", secret_action)

print(access_secret("wrong_pass")) # Expected output: Invalid password.
print(access_secret("password123")) # Expected output: The secret code is 1234.

# problem 9
def make_rate_limiter(max_calls):
    counter = 0
    def func():
        nonlocal counter
        counter += 1
        if counter <= max_calls:
            return 'Accepted'
        return 'Rejected'
    return func
# Example usage:
limiter = make_rate_limiter(2)
print(limiter())  # Expected output: Accepted
print(limiter())  # Expected output: Accepted
print(limiter())  # Expected output: Rejected

limiter2 = make_rate_limiter(1)
print(limiter2()) # Expected output: Accepted
print(limiter2()) # Expected output: Rejected
print(limiter())  # Still Rejected

# problem 10
def memoize(func):
    results = {}
    def memoize_func(*args):
        if (args) in results.keys():
            return results[(args)]
        computed_value = func(*args)
        results[(args)] = computed_value
        return computed_value

    return memoize_func
# Example usage:
def add(a, b):
    print("Computing...")
    return a + b

memoized_add = memoize(add)

print(memoized_add(2, 3)) # Prints "Computing..." then "5"
print(memoized_add(2, 3)) # Prints "5"
print(memoized_add(5, 5)) # Prints "Computing..." then "10"
print(memoized_add(5, 5)) # Prints "10"