# problem 1
reciprocals = (1 / num for num in range(1, 11))
for num in reciprocals:
    print(num)

# problem 2
def reciprocals(num):
    count = 1
    while count <= num:
        yield 1 / count
        count +=1

for num in reciprocals(7):
    print(num)

# problem 3
# The main syntactical difference between a list comprehension and a generator expression lies in the brackets
# list comprehensions use square brackets, [], while generator expressions use parentheses, ()
# This reflects the fact that a list comprehension creates a new list object, while a generator expression creates a generator object

# problem 4
# If you try to iterate over a generator a second time, Python will raise a StopIteration Error.
# This indicates that the generator has been exhausted, and has no more values left to yield
# This behavior is a consequence of a generator object not holding enough state to calculate more than one value at a time.
# Thus, if you want to iterate over a generator a second time, you must recreate the generator object anew.

# problem 5
numbers = (number for number in [1, 3, 5, 7, 9, 11])

print("First loop:")
for number in numbers:
    print(number)
    if number >= 5:
        break

print('Finished the first loop')

print("Second loop:")
for number in numbers:
    print(number)

# This will print
# "First Loop"
# 1
# 3
# 5
# "Finished the first Loop"
# "Second Loop"
# 7
# 9
# 11

# After the first loop is complete, the generator object has yielded three values, however, it is not exhausted.
# Thus, when the second loop starts, it continues yielding values from where it left off
# Eventually, it will throw a StopIteration Error, but this is taken care of automatically by the for loop

# problem 6
print(char.upper() for char in 'launch')
# print(42, char.upper() for char in 'launch')

# The first print statement will output a string representation of a generator object, since that is a generator expression that creates a generator object
# This will typically look like "generator object <genexpr> at <memory address>"\
# The second line, if uncommented and run, will return a SyntaxError.
# You are allowed to remove parentheses when passing generators as function arguments only when the generator is the sole argument. Otherwise, you do need parentheses around the generator.

# problem 7
def capitalize_short(strings):
    for word in strings:
        if len(word) < 5:
            yield word.capitalize()

words = ['four', 'score', 'and', 'seven', 'years', 'ago']
print(set(capitalize_short(words)))

# problem 8
# Since a generator only holds enough state to compute one value when requested, it does not contain a sequence.
# Thus, it is not possible to access a specific value in a generator through indexing, since there is no sequence to index through
# Furthermore, it is equally impossible for other sequencing operations like slicing or `len()` to work

# problem 9
# It is possible to create a generator that never runs out of values, like so:
def infinite_numbers_by_two():
    counter = 2
    while True:
        yield counter
        counter += 2

# THe primary risk in an infinite generator is working with the values yielded.
# If the numbers become too large, then you may run out of memory.
# If you need to iterate over numbers previously yielded, there's no way to go back


# problem 10
def my_reduce(callback, iterable, initial_value):
    accum = initial_value
    for item in iterable:
        accum = callback(accum, item)

    return accum

print(my_reduce(lambda accum, item: accum + (item ** 3),
                (num for num in range(1, 11)),
                0))


