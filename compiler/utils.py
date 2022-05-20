# -*- encoding :: utf-8 -*-

class Stack:
    def __init__(self):
        self.values = []

    def is_empty(self):
        return len(self.values) == 0

    @property
    def back(self):
        if not self.is_empty():
            return self.values[-1]

    def push(self, value):
        self.values.append(value)

    def pop(self):
        if not self.is_empty():
            return self.values.pop()


def load_file(path: str):
    with open(path, 'r', encoding='utf-8') as file:
        return file.read()
