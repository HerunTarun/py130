# problem 1
def combine(num1, num2, num3):
    return (num1, num2, num3)

print(combine(1, 2, 3))
# problem 2
def multiply(num1, num2, /):
    return num1 * num2

print(multiply(2, 3))
try:
    print(multiply(num1=3, num2=2))
except TypeError:
    print('TypeError expected!')
# problem 3
def describe_pet(animal_type, *, name=''):
    if not name:
        print(f'This is an unnamed {animal_type}')
    else:
        print(f'This is a {animal_type} named {name}')


describe_pet('cat')
describe_pet('cat', name='mary')
try:
    describe_pet('cat', 'jane')
except TypeError:
    print('TypeError expected')
try:
    describe_pet('cat', 'mary', name='jane')
except TypeError:
    print('TypeError expected!')

# problem 4
def calculate_average(*num):
    if not num:
        return None
    return sum(num) / len(num)

print(calculate_average(1, 2, 3, 4, 5, 6, 7, 8, 9))
print(calculate_average())

# problem 5
def find_person(**kwargs):
    if 'antonina' in kwargs:
        print(f"antonina's profession is {kwargs['antonina']}")
    else:
        print('antonina not found')


find_person(victor='TA', pete='TA', antonina='TA')
print()
find_person(victor='TA', pete='TA')


# problem 6
def concat_strings(*args, sep=' '):
    return sep.join(args)


print(concat_strings('blink', 'and', "it's", 'gone'))
print(concat_strings('blink', 'and', "it's", 'gone', sep=', '))

# problem 7
def register(username, /, age, *, password):
    return {
        'username': username,
        'password': password,
        'age': age
    }

print(register('herun', password='blech', age=35))
print(register('herun', 35, password='blech'))

# problem 8
def print_message(*, message, level='INFO'):
    print(f'{level} {message}')

print_message(message='help')
print_message(level='emergency', message='help')
print_message('help')
