class Todo:
    COMPLETE_MARKER = 'X'
    INCOMPLETE_MARKER = ' '

    def __init__(self, title, done=False):
        self._title = title
        self.done = done

    @property
    def title(self):
        return self._title

    @property
    def done(self):
        return self._done

    @done.setter
    def done(self, new_state):
        self._done = new_state

    def _check_status(self):
        if self.done:
            return Todo.COMPLETE_MARKER
        return self.INCOMPLETE_MARKER

    def __str__(self):
        return f'[{self._check_status()}] {self.title}'

    def __eq__(self, other):
        if not isinstance(other, Todo):
            return NotImplemented

        return (self.title == other.title) and (self.done == other.done)

    def __ne__(self, other):
        if not isinstance(other, Todo):
            return NotImplemented

        return (self.title != other.title) and (self.done != other.done)