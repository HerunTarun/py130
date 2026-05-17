# problem 1
# A pure function is a function that has no side effects and, given the same set of arguments, always returns the same value during the function's lifetime.
# The second requirement implies that the return value of a pure function depends solely on its arguments, i.e nothing else in the program can influence the function within its lifetime.

# problem 2
items = [1, 2, 3]

def process_items(new_item):
    items.append(new_item)
    return len(items)
# in this case, this is not a pure function. Since the return value does not depend on the arguments, but rather an object referenced by a global variable,
# this contravenes one of thw two defining properties of a pure function.
# In this case, it also performs a side effect through mutation, which also makes it ineligible as a pure function.

# problem 3
def update_records(record_id, data, file_path='records.txt'):
    print(f"Updating record {record_id}...")
    with open(file_path, 'a') as f:
        f.write(f"{record_id}:{data}\n")
        data.update({'status': 'updated'})
    return data
# here, we have side effects through input/output(I/O) operators from the print statement
# we also have another input/output side effect coming from the context manager opening a file
# inside the context manager, we have another input/output side effect coming from writing to a file
# lastly, we update an object passed in through the 'data' parameter, which is a side effect through mutation

# problem 4
import datetime

def get_greeting():
    current_hour = datetime.datetime.now().hour
    if 5 <= current_hour < 12:
        return "Good morning"
    elif 12 <= current_hour < 18:
        return "Good afternoon"
    else:
        return "Good evening"

# this function is not a pure function, since this is a side effect through other functions.
# The expression assigned to current_hour is evaluated using a function from the datetime module
# However, the datetime.now() function is a function with a side effect
# Since that side effect propagates outside of get_greeting(), we can safely call this not a pure function
# Moreover, since the return value changes independent of any arguments, it violates a core property of a pure function

# problem 5
# Yes, it can. The definition of a pure function is that it has no side effects and has a consistent return value for a given set of arguments.
# As long as the function abides by those properties, it is a pure function.
# def do_nothing(value):
# 	pass
# Here, the function `do_nothing()` takes an argument `value` and implicitly returns `None`.
# It has no side effects, and it will always return `None` if you pass the same argument to it.

# problem 6
def create_user(username, details_list):
    user_profile = {
        'username': username
        }
    details_list.reverse()
    user_profile['preferences'] = details_list
    return user_profile
# No, this is not a pure function. This function mutates the object assigned to details_list, which is a side effect through mutation
# Thus, it is not a pure function, since it contravenes the first property of a pure function, that it have no side effects.

# problem 7
def add_to_team(team_members, new_member):
    team_members.append(new_member)
    return team_members
# This is not a pure function, since the function is mutating the object assigned to team_members, which is a side effect through mutation
# If the caller assumes it is pure, it may lead to unexpected errors arising from the fact that the length of the object assigned to team_members has been changed
#
# problem 8
data_store = [1, 2, 3, 4]

def process_data(data):
    return [num ** 2 for num in data]

process_data(data_store)

# problem 9
# pure functions are easier to test than impure functions, because you can both rely on their output to be consistent, and work with the knowledge that the function does not have effects propagating out to the rest of the codebase
# for example, take these two functions:
results = []
def impure_func(num):
    results.append(num ** 2)
# test that results is empty
# reset results before each test
#

def pure_func(num):
    return num ** 2

# test that

# problem 10
# a method that modifies an instance's state is a function that has a side effect through mutation, since we're modifying the value of an object not local to the function
# second, an instance method's implicit first argument, self, always refers to the object. Thus, a method that modifies self can produce different results with every call even if the argument is identical, since the state of self is constantly being updated

class ShoppingCart:
    def __init__(self, items=None):
        self.items = items if items is not None else []

    def add_item(self, item, price):
        self.items.append({'item': item, 'price': price})

    def calculate_total(self):
        return sum(item['price'] for item in self.items)

