class Task:
    id: int
    title: str
    done: bool = False

    def __init__(self, id: int, title: str, done: bool = False):
        self.id = id
        self.title = title
        self.done = done
