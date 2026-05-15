# problem 1
# The output would be a loop
# Executing module_a
# Executing module b
# Executing module a

# problem 2
# an absolute import would be importing a module using an absolute path
# while a relative import would be importing a module using a path relative to the script you're working in
# here, `main.py` could import the helper function in `utils.py` using an absolute path, like so:
# import helper from my_project/my_app/utils.py
# or a relative path, like so:
# import helper from utils

# problem 3
# `if __name__ == '__main__' is a code block that runs the entire program when the file is being run as a script, rather than a module, and does nothing otherwise.
# This makes the file dual-purpose.
# You can run the file from the command line as a script or as a module imported into another program.
# This is especially useful in two scenarios:
# first, you can store tests in this block to run unit and regression tests when you're maintaining the module
# second, you can store execution logic that you don't want imported inside the code block

# problem 4
# The `import` keyword allows you to write an import statement, which allows you to load code from a Python module into your code.
# Any function or constant we use from the module is prefixed with the module's name, so my_module.my_function()
# On the other hand, the `from` keyword allows you to import identifiers directly from a module into your program.
# This bypasses the need to prefix your attributes with the module's name, so my_function()
# However, if you are using the `from` keyword, you cannot access an attribute from the module if it's not specified
# This allows you to avoid namespace pollution, where you control exactly which identifiers are available in your script.

# problem 5
# walk through problem 5 with me, relating it to concepts in the py130 lessons
# problem 6

# problem 7

# problem 8

# problem 9

# problem 10
