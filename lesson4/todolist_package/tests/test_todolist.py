import unittest
from todolist import Todo, TodoList

class TestTodoList(unittest.TestCase):
    def setUp(self):
        self.todo1 = Todo("Buy milk")
        self.todo2 = Todo("Clean room")
        self.todo3 = Todo("Go to the gym")

        self.todos = TodoList("Today's Todos")
        self.todos.add(self.todo1)
        self.todos.add(self.todo2)
        self.todos.add(self.todo3)

    def test_length(self):
        self.assertEqual(3, len(self.todos))

    def test_to_list(self):
        # check test object truth against function return value
        self.assertEqual([self.todo1, self.todo2, self.todo3],
                         self.todos.to_list())

    def test_first(self):
        self.assertEqual(self.todo1, self.todos.first())

    def test_last(self):
        self.assertEqual(self.todo3, self.todos.last())

    def test_all_done(self):
        # feel free to modify your test object's attributes so that you can test
        self.todos.mark_all_done()
        self.assertTrue(self.todos.mark_all_done())

    def test_add_invalid(self):
        # correct, but not great
        # self.assertRaises(TypeError, self.todos.add, 'string')
        # better version
        with self.assertRaises(TypeError):
            self.todos.add('string')

    def test_todo_at(self):
        self.assertEqual(self.todo1, self.todos.todo_at(0))
        self.assertEqual(self.todo2, self.todos.todo_at(1))
        self.assertEqual(self.todo3, self.todos.todo_at(2))
        # remember to check for errors
        with self.assertRaises(IndexError):
            self.todos.add(5)

    def test_mark_done_at(self):
        self.todos.mark_done_at(0)
        self.assertTrue(self.todo1.done)
        with self.assertRaises(IndexError):
            self.todos.mark_done_at(5)
        # remember to also check that other values remained unchanged
        self.assertFalse(self.todo2.done)
        self.assertFalse(self.todo3.done)

    def test_mark_undone_at(self):
        self.todo1.done = True
        self.todo2.done = True
        self.todo3.done = True

        self.todos.mark_undone_at(0)
        with self.assertRaises(IndexError):
            self.todos.mark_undone_at(5)

    def test_mark_all_done(self):
        self.todos.mark_all_done()

        self.assertTrue(self.todo1.done)
        self.assertTrue(self.todo2.done)
        self.assertTrue(self.todo3.done)
        # you could test the following if you didn't have a test for the query method
        # the gist is: have a test for every public method, either combined or separate
        self.assertTrue(self.todos.all_done())

    def test_remove_at(self):
        with self.assertRaises(IndexError):
            self.todos.remove_at(5)

        self.todos.remove_at(0)
        self.assertEqual(2, len(self.todos))
        self.assertEqual('Clean room', self.todos.first().title)
        # better version
        self.assertEqual([self.todo2, self.todo3], self.todos.to_list())

    def test_str(self):
        # expected_header = f"---- {self.title} ----\n"
        # formatted_todo = [str(item) for item in self.todos.to_list()]
        # expected_str =  expected_header + "\n".join(formatted_todo)

        # don't rebuild your method logic, test against an objective truth
        expected_str = (
            "----- Today's Todos -----\n"
            "[ ] Buy milk\n"
            "[ ] Clean room\n"
            "[ ] Go to the gym"
        )
        self.assertEqual(expected_str, str(self.todos))

    def test_str_done_todo(self):
        expected_str = (
            "----- Today's Todos -----\n"
            "[X] Buy milk\n"
            "[ ] Clean room\n"
            "[ ] Go to the gym"
        )
        self.todos.mark_done_at(0)
        self.assertEqual(expected_str, str(self.todos))

    def test_str_all_done_todos(self):
        expected_str = (
            "----- Today's Todos -----\n"
            "[X] Buy milk\n"
            "[X] Clean room\n"
            "[X] Go to the gym"
        )

        self.todos.mark_all_done()
        self.assertEqual(expected_str, str(self.todos))

    def test_each(self):
        # always remember to check whether the function has a side effect or return value
        # then test accordingly
        check_list = []
        self.todos.each(lambda todo: check_list.append(todo))
        self.assertEqual([self.todo1, self.todo2, self.todo3], check_list)

    def test_select(self):
        self.todos.mark_done_at(0)
        selected = self.todos.select(lambda todo: todo.done)
        self.assertEqual([self.todo1], selected.to_list())


if __name__ == "__main__":
    unittest.main()