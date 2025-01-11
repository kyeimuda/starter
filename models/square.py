#!/usr/bin/python3
from models.rectangle import Rectangle

class Square(Rectangle):
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    def __str__(self):
        return f'[{__class__.__name__}] ({self.id}) {self.x}/{self.y} - {self.width}'

    @property
    def size(self):
        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        if args:
            if len(args) == 1:
                self.id = int(args[0])
            elif len(args) == 2:
                self.id = int(args[0])
                self.size = int(args[1])
            elif len(args) == 3:
                self.id = int(args[0])
                self.size = int(args[1])
                self.x = int(args[2])
            else:
                self.id = int(args[0])
                self.size = int(args[1])
                self.x = int(args[2])
                self.y = int(args[3])
        else:
            if kwargs:
                for attr, value in kwargs.items():
                    setattr(self, attr, value)

    def to_dictionary(self):
        return self.__dict__
