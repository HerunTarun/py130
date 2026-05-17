# problem 1
# the purpose of the if __name__ == '__main__': unittest.main() is to run the tests in the file if the file is being run as a script
# this ensures that the tests are not run if the file was imported as a module

# problem 2
# The SEAT approach describes the four steps of structuring a test, where:
# S stands for: Set up the necessary objects
# This is where you can use the setUp method.
# It creates a clean, consistent environment for each test by executing before every `test_` method.
# This guarantees every test starts with a fresh, identical object, preventing the outcome of any single test from affection another.
# The `setUp` method often contains logic that instantiates a mock object with specific state for your tests.
# E stands for: Execute the code against the object you're testing
# The E in the SEAT approach generally refers to the specific action within a test method that runs the code we are testing.
# This often happens on the same line as Assert.
# For example, in the line `self.assertEqual(4, self.car.wheels)`, `self.car.wheels` is the Execute step.
# A stands for: Assert that the executed code did the right thing
# The A in the SEAT approach generally refers to writing assertions in your tests.
# When using the `unittest` module, this generally refers to using the various assertions, e.g. `assertEqual()` in our tests.
# T stands for: Tear down and clean up any lingering artifacts.
# The T in the SEAT approach generally refers to cleaning up files, logging information or closing database connections.
# When using the `unittest` module, this generally refers to using the `tearDown` method, which is called after running each test.
# It's mainly used to make sure that the test environment is left pristine for the next test.
# Thus, it's sometimes not necessary if the tests don't create any lasting side effects, like creating files or holding open database connections.

# problem 3
import unittest
import string_utils

class TestMain(unittest.TestCase):
    def setUp(self):
        self.func = string_utils.to_title_case

    def test_typical_sentence(self):
        self.assertEqual('This Is Sparta', self.func('this is sparta'))

    def test_empty_string(self):
        self.assertEqual('', self.func(''))

    def test_sentence_already_titlecase(self):
        self.assertEqual('This Is Sparta', self.func('This Is Sparta'))

    def test_type_checking(self):
        with self.assertRaises(TypeError):
            self.func(13223)
if __name__ == '__main__':
    unittest.main()

# problem 4
# The setUp method creates a clean, consistent environment for each test by executing before every `test_` method.
# This guarantees every test starts with a fresh, identical object, preventing the outcome of any single test from affection another.
# The `setUp` method often contains logic that instantiates a mock object with specific state for your tests.
# For example, if you were testing the following class:
class Person:
    def __init__(self, name):
        self.name = name

    def get_name(self):
        return self.name

    def change_name(self, new_name):
        self.name = new_name

class TestPerson(unittest.TestCase):
    def setUp(self):
        self.person = Person('tom')

    def test_name_getter(self):
        self.assertEqual('tom', self.person.get_name())

    def test_name_changer(self):
        self.person.change_name('harry')
        self.assertEqual('harry', self.person.get_name())

# Here, using setUp allows us to ensure that the two tests are independent, since setUp runs before each test, ensuring a fresh Person object for each test

# The tearDown method is mainly used to make sure that the test environment is left pristine for the next test.
# It is called after each test to clean up files, log information, or close database connections
# Thus, it's sometimes not necessary if the tests don't create any lasting side effects, like creating files or holding open database connections.

# problem 5
# The fundamental difference between self.assertEqual(a, b) and self.assertIs(a, b) assertion methods fall back to what they rely on. assertEqual uses the equality operator, while assertIs uses the identity operator
# The identity operator `is` compares the identity of two objects in memory.
# # This allows one to check whether two objects that may have similar state are actually two distinct objects in memory.

# Although it looks similar in function to the equality operator `==`, they answer two very different questions.
# Namely, equality checks whether the state of two objects are equal, while identity checks whether the two objects are distinct.
# Here's an example where assertEqual passes, but assertIs fails
class Data:
    def __init__(self, data1, data2):
        self.data1 = data1
        self.data2 = data2

data_1 = [1, 2, 3, 4]
data_2 = [1, 2, 3, 4]

class DataTest(unittest.TestCase):
    def setUp(self):
        self.obj = Data(data_1, data_2)

    def test_equality(self):
        self.assertEqual(self.obj.data1, self.obj.data2)

    def test_identity(self):
        self.assertIs(self.obj.data1, self.obj.data2)

# On the other hand, here's an example of where both tests pass
class Data:
    def __init__(self, data1, data2):
        self.data1 = data1
        self.data2 = data2

data_1 = [1, 2, 3, 4]
data_2 = data_1

class DataTest(unittest.TestCase):
    def setUp(self):
        self.obj = Data(data_1, data_2)

    def test_equality(self):
        self.assertEqual(self.obj.data1, self.obj.data2)

    def test_identity(self):
        self.assertIs(self.obj.data1, self.obj.data2)


# problem 6
def calculate_average(numbers):
    if not numbers:
        raise ValueError("Input list cannot be empty")
    return sum(numbers) / len(numbers)

class AverageTest(unittest.TestCase):
    def setUp(self):
        self.obj = calculate_average

    def test_ValueError(self):
        with self.assertRaises(ValueError):
            self.obj([])

if __name__ == '__main__':
    unittest.main()

# problem 7
# skip because it deals with running specific test methods and test classes

# problem 8
# We have them because specialized assertions make tests clearer to readers by showing intent directly.

# They also produce more specific error output, which can be more helpful in testing.

# Lastly, some specialized assertions do extra checks or are optimized for particular situations (e.g. checking membership).
# This specific behavior is lost if you use a general assertion method like `assertTrue()`.
# If you need a specific assertion method, perusing the `unittest` documentation is your best bet.

# problem 9
class Cart:
    def __init__(self):
        self.items = []

    def add_item(self, item):
        self.items.append(item)

    def get_item_count(self):
        return len(self.items)

class TestCart(unittest.TestCase):
    def setUp(self):
        self.my_cart = Cart()

    def test_add_one_item(self):
        self.my_cart.add_item("apple")
        self.assertEqual(['apple'], self.my_cart.items)

    def test_add_second_item(self):
        self.my_cart.add_item("apple")
        self.my_cart.add_item("banana")
        self.assertEqual(['apple', 'banana'], self.my_cart.items)

    def test_item_count(self):
        self.my_cart.add_item("apple")
        self.my_cart.add_item("banana")
        self.assertEqual(2, self.my_cart.get_item_count())

if __name__ == '__main__':
    unittest.main()

# problem 10
# skip because it deals with unittest.mock.patch