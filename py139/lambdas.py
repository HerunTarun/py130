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
# 6
# 6
# 6
# 6
# 6
# This is an example of late binding in lambdas.
# Here, `create_multiplier()` is return a list of lambdas, iterating over a sequence of numbers from 0 to 4. When doing so, the lambda captures a reference to the loop variable i
# However, the value of the loop variable is not captured upon each iteration of the loop
# Rather, only a reference to that loop variable is captured.
# Thus, when the lambda is called in the for loop with the argument 2, it is only then that it evaluates the value of the loop variable, which is now 4


# problem 7
import time

def report_time(get_time=lambda: time.time()):
    print(f"Timestamp: {get_time()}")

report_time()
time.sleep(1)
report_time()

# problem 8
# problem 9
# problem 10