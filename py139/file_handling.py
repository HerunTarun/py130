# problem 1
# The `open(file_path_name, mode)` function is a built-in Python function used to work with files.
# It opens a file and returns a file object that you can read from or write to.
# This file object returned by `open()` is an iterator.
# The file path name used by `open()` is a relative path, but you can also provide an absolute path if you want.
# It takes two arguments, a string representing the file's path name, and a string representing the mode (r, w, a).
# 'r' stands for read, allowing you to read the file, 'w' stands for write, which truncates the file and writes to it, and 'a' stands for append, which appends to the file.
# problem 2
# 'r' stands for read, allowing you to read the file. It does not allow you to write to the file
# 'w' stands for write, which truncates the file and writes to it. This is dangerous, since it erases the contents of the file before you write anything.
# 'a' stands for append, which appends to the file.
# problem 3
with open('hello.txt', 'w') as f:
    f.write('Hello, world!\n')
# problem 4
# It's important to close a file once you're done with it.
# Otherwise, the resources allocated to file handling are not returned to your system or the application.
# These resources are surprisingly limited and can run out quickly.
# You can close a file using the close method, like so: f.close() or by using a context manager like the `with` keyword, which automatically closes the file.

# problem 5
with open('log.txt', 'w') as file:
    file.write('Log entry 1\n')
    # some other processing happens here that might raise an error
    file.write('Log entry 2\n')
    file.write('Log entry 3\n')

# problem 6
def count_lines(filepath):
    try:
        with open(filepath, 'r') as f:
            return sum(1 for line in f)
    except FileNotFoundError:
        return 0

# problem 7
# the contents of data.txt would be:
# dog
# cat
# Opening the files in `w` mode would have erased the contents of data.txt first
# Then, it would have written 'dog\n'
# Then, the context manager would have closed the file
# When reopened in `a` mode, we can append contents to file
# which is when we appended 'cat\n'
# The addition of the newline characters would put dog and cat on separate lines
# giving us the final contents of data.txt as:
# dog
# cat

# problem 8
with open('report.txt', 'r') as file:
    with open('report_copy.txt', 'w') as file_copy:
        for index, line in enumerate(file, 1):
            file_copy.write(f'{index}: {line}')

# problem 9
def get_config_value(filepath, key):
    with open(filepath, 'r') as file:
        for line in file:
            current_key, value = line.split('=')
            if current_key == key:
                return value

    return None
# problem 10
def merge_files(file_list, output_file):
    with open(output_file, 'w') as output:
        for file in file_list:
            try:
                with open(file, 'r') as source:
                    output.writelines(source.readlines())
                    output.write('----------\n')
            except FileNotFoundError:
                continue
