# problem 1
# When compared to a function defined with the `def` keyword, a lambda function is smaller, since it fits on one line
# It also has no need for the `return` keyword since it implicitly returns the value of the expression within it
# However, that advantage in size does come with a few drawbacks.
# For one, a lambda function can only have a single expression.
# They cannot include assignment, loops, or statements like if.
# They cannot include docstrings.
# Lastly, they are difficult to debug because they don't have names that would show up in a traceback

# problem 2
multiply = lambda num1, num2: num1 * num2
print(multiply(2, 3))

# problem 3
# a lambda function can only have a single expression, which cannot include assignment, loops, or statements like if.
# This is because a lambda function is built such that it only takes up a single line
# However, while you cannot write an if statement in a lambda, you can use a ternary expression, since a ternary expression can be evaluated to a value in a single line.

# problem 4
words = ['hello', 'world', 'python']
print(list(map(lambda word: word.upper(), words)))

# problem 5
people = [
        {'name': 'Alice', 'age': 30, 'city': 'New York'},
        {'name': 'Bob', 'age': 25, 'city': 'Los Angeles'},
        {'name': 'Charlie', 'age': 35, 'city': 'Chicago'},
        {'name': 'Alice', 'age': 25, 'city': 'Chicago'}
        ]
print(sorted(people, key=lambda person: (person['age'], person['name'])))

# problem 6
def create_multipliers():
        return [lambda x: i * x for i in range(5)]

for multiplier in create_multipliers():
    print(multiplier(2), end=' ')
# This will print:
# 8 8 8 8 8
# This is an example of late binding in lambdas.
# Here, `create_multiplier()` is return a list of lambdas, iterating over a sequence of numbers from 0 to 4. When doing so, the lambda captures a reference to the loop variable i
# However, the value of the loop variable is not captured upon each iteration of the loop
# Rather, only a reference to that loop variable is captured.
# Thus, when the lambda is called in the for loop with the argument 2, it is only then that it evaluates the value of the loop variable, which is now 4


# problem 7
import time

def report_time(get_time=lambda: time.time()):
    print(f"Timestamp: {get_time()}")

report_time() # returns a floating point number representing time
time.sleep(1)
report_time() # returns a floating point number that's roughly one second later than earlier

# Here, we have a lambda assigned as the default value in a parameter `get_time` in a function `report_time()`
# It is at this moment, when the function is defined, that the lambda argument is created.
# The expression within the lambda is not evaluated at the time of its definition, but rather when the print statement is executed
# Thus, since we're called `report_time()` twice, with a call to `time.sleep(1)` that suspends program flow for 1 second,
# we will find that the twin calls of `report_time()` are 1 second apart, which will be roughly reflected in their return values

# problem 8
factorial_logic = lambda f, num: 1 if num in [0, 1] else num * f(f, num -1)
factorial = lambda n: factorial_logic(factorial_logic, n)
print(factorial(5))

# problem 9
def compose(f, g):
    return lambda x: f(g(x))

def create_list(numbers):
    return list(numbers)

list_then_sum = compose(sum, create_list)

print(list_then_sum(range(1,6)))

# problem 10
# Lexical scope is a term for the environment in which a function is defined. It is determined by the actual layout of the code, since it can be a global scope, or simply a nonlocal scope.
# For example:
def create_greeting():
    greeting = 'hello'

    def display_greeting():
        print(greeting)

    return display_greeting

greet = create_greeting()
greet()  # Output: Hello
# Here, the lexical scope of `display_greeting()` is the scope of `create_greeting()`, while the lexical scope of `create_greeting()` is the global scope.