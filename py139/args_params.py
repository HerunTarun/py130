# problem 1
def add_to_list(value, my_list=[]):
    my_list.append(value)
    return my_list

print(add_to_list(1)) # [1]
print(add_to_list(2)) # [1, 2]
print(add_to_list(3, [10, 20])) # [1, 2, 3, [10, 20]]
print(add_to_list(4)) # [1, 2, 3, [10, 20], 4]
# This is a common problem with mutable default arguments.
# Python will use the same object for all calls to that function, rather than a new mutable object
# Thus, every invocation of the function only mutates the object, rather than starting from a new mutable object.

# problem 2
def process_data(a, *b, c):
    print(f"a: {a}")
    print(f"b: {b}")
    print(f"c: {c}")
# The first parameter, a, is a positional parameter, which is supplied by the first argument in process_data()'s invocation
# The second parameter, *b, actually collects all remaining positional arguments into a tuple. This is conventionally named args, but here is simply named b
# The third paramater, c, is actually a keyword parameter, which means it can only be supplied by keyword in the function invocation
# A valid function call would look like the following:
process_data('anything', 'but', 'for', 'the', 'grace', 'of', c='god')
# here, we pass in 'anything' through the parameter a, while b collects the remaining positional arguments in a tuple, and lastly, we pass in 'god' through the keyword c
# an invalid function call would look like the following:
# process_data('anything', 'but', 'for', 'god')
# here we attempt to pass in 'god' as a positional argument, but this will raise a TypeError, since it is a required keyword-only argument


# problem 3
def create_user(username, email, *groups, admin=False, **profile_info):
    user = {
            'username': username,
            'email': email,
            'groups': groups,
            'admin': admin,
            'profile': profile_info
    }
    return user

base_data = ('jdoe', 'jdoe@example.com')
extra_groups = ['editors', 'reviewers']
profile_details = {'country': 'USA', 'city': 'New York'}

print(create_user(*base_data, *extra_groups, admin=True, **profile_details))
# the output will be:
# {'username': 'jdoe', 'email': 'jdoe@example.com', 'groups': ('editors', 'reviewers'), 'admin': True, 'profile': {'country': 'USA', 'city': 'New York'}}
# here, we're using argument unpacking to unpack tuples into the corresponding parameters in the function call.
# the tuple assigned to base_data is unpacked into the positional parameters `username`, and `email`
# the elements in the list assigned to extra_groups is collected into a tuple by the parameter *groups,
# the Boolean True is assigned to the admin parameter, in lieu of the default value False
# and the key-value pairs in the dictionary assigned to profile_details is collected into a dictionary by the parameter **profile_info.
# These are then inserted into the dictionary user and returned
# It's important to note that the keys groups and profile in the user dict have the tuple and dictionary object collected by *extra_groups and **profile_details respectively assigned to them
# Here, we also see the use of the * and ** operators in the function call to unpack the values in a list and a dictionary, respectively, into the function parameters *groups, and **profile_details

# problem 4
def calculate_area(length, width, /):
    return length * width
# Here, the developer has chosen to enforce positional-only arguments in this function by using the `/` marker.
# This denotes that any parameters preceding the marker can only be supplied by position, rather than by keyword.
# A developer might choose to do so when they have a small number of arguments and the parameter order is intuitive.
# An exmaple of a call that works would be:
calculate_area(7, 8)
# while an example of a call that would fail would be:
# calculate_area(9, width=5)
# Here, we're attempting to pass the integer 5 in as a keyword argument, however, the function definition has already indicated that all arguments are positional-only

# problem 5
def display_config(font='Arial', **kwargs):
    config = {'font': font}
    config.update(kwargs)
    for key, value in sorted(config.items()):
        print(f"{key}: {value}")

display_config(color='blue', font='Times New Roman', size=12)
# this will print:
# color: blue
# font: Times New Roman
# size: 12
# Here, since we have defined font as a named parameter, Python will accept keyword arguments and positional arguments unless it's designated as positional-only syntaxes when invoking the function
# However, it is important to note that if you pass in a positional argument to font, then it must come before you pass in any keyword arguments
# The contents of the kwargs dictionary within display_config() are as follows:
# {
#     'color': 'blue'
#     'size': 12
# }
# The kwargs dictionary uses the keyword as a key and the value assigned to the keyword as the value in the dictionary

# problem 6
# def create_report(title, author, **details, date):
#     print(f"Report '{title}' by {author} on {date}.")
#     print(f"Details: {details}")

# This raises a Syntax error since you're defining a named parameter after **details
# Since all keyword arguments come after positional arguments, and **details collects all remaining keyword arguments into a dictionary
# there should not be any more parameters succeeding **details
def create_report(title, author, *, date, **details):
    print(f"Report '{title}' by {author} on {date}.")
    print(f"Details: {details}")
# This allows date to be a keyword-only parameter, since we're using the * marker, which denotes that any suceeding parameter is keyword-only

# problem 7
def setup_project(project_id, /, owner, *, deadline, **options):
    print(f"ID: {project_id}, Owner: {owner}, Deadline: {deadline}")
    print(f"Options: {options}")

# setup_project('proj-123', owner='Alice', '2024-12-31', priority='High')
# This call raises a SyntaxError since deadline is defined in the function definition as a keyword-only parameter.
# This is denoted by the * marker, which indicates that any suceeding parameter is keyword-only
setup_project('proj-123', owner='Alice', deadline='2024-12-31', priority='High')
# This function call would be valid

# problem 8
def process_items(source_id, /, *items, mode='strict', retries, **options):
    return {
        'source_id': source_id,
        'items': items,
        'mode': mode,
        'retries': retries,
        'options': options,
    }

print(process_items(12345, 'boxes', 'shelves', mode='relaxed', retries=4, timeout=30, verbose=True))
# problem 9
def log_message(level, /, timestamp, *, message, **metadata):
    pass

log_message('INFO', '2023-10-27T10:00:00Z', message='Login success', user_id=101, session_id='xyz')
# level - positional only, argument passed in - 'INFO'
# timestamp - positional or keyword, argument passed in - '2023-10-27T10:00:00Z'
# message - keyword only, argument passed in - 'Login success'
# **metadata - collects all remaining keyword arguments into a dictionary, arguments passed in - user_id=101, session_id='xyz'
# if the call was changed to level='INFO', it would raise a SyntaxError, since level is a positional only parameter
# problem 10
def arg_logger(func):
    def wrapper(*args, **kwargs):
        print(func.__name__)
        print(args)
        print(kwargs)
        result = func(*args, **kwargs)
        return result

    return wrapper
@arg_logger
def add_salutation(title, name, *, suffix="PhD", informal=False):
    salutation = f"Hello, {title} {name}"
    if not informal:
        salutation += f", {suffix}"
    return salutation

# Example call after decoration:
print(add_salutation("Dr.", "Jane Smith", informal=True, suffix="MD"))
