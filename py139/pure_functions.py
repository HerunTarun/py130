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
# No, a function that never returns a value
# problem 6

# problem 7

# problem 8

# problem 9

# problem 10
