from todo import Todo

class TodoList:
    def __init__(self, title):
        self._title = title
        self._todos = []

    @property
    def title(self):
        return self._title

    def add(self, todo):
        if not isinstance(todo, Todo):
            raise TypeError('Todo item must be a Todo object!')
        self._todos.append(todo)

    def __str__(self):
        formatted_todo = [str(item) for item in self._todos]
        heading = f"---- {self.title} ----\n"
        return heading + "\n".join(formatted_todo)

    def __len__(self):
        return len(self._todos)

    def first(self):
        return self._todos[0]

    def last(self):
        return self._todos[-1]

    def to_list(self):
        return list(self._todos)

    def todo_at(self, index):
        return self._todos[index]

    def mark_done_at(self, index):
        self.todo_at(index).done = True

    def mark_undone_at(self, index):
        self.todo_at(index).done = False

    def mark_all_done(self):
        def mark_done(todo):
            todo.done = True

        self.each(mark_done)

    def mark_all_undone(self):
        def mark_undone(todo):
            todo.done = False

        self.each(mark_undone)

    def all_done(self):
        return all([item.done for item in self._todos])

    def remove_at(self, index):
        self._todos.pop(index)

    def each(self, callback):
        for item in self._todos:
            callback(item)

    def select(self, callback):
        selected_items = TodoList(self.title)

        def pick_item(todo):
            if callback(todo):
                selected_items.add(todo)

        self.each(pick_item)

        return selected_items

    def find_by_title(self, title):
        matching_todos = self.select(lambda todo: todo.title == title)
        return matching_todos.first()

    def done_todos(self):
        return self.select(lambda todo: todo.done)

    def undone_todos(self):
        return self.select(lambda todo: not todo.done)

    def mark_done(self, title):
        self.find_by_title(title).done = True