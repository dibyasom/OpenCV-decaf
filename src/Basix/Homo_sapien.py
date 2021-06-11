from typing import ClassVar, overload


class human:
    __is_dumb = False
    talks = True
    name = ""

    def __init__(self, name, talks) -> None:
        self.name = name
        self.talks = talks

    @classmethod
    def is_dumb(cls):
        if(cls.__brain_type):
            print("Dumb!")
        else:
            print("Not dumb!")

    def __str__(self):
        return "Class Human"

    def can_talk(self):
        if(self.talks):
            print(f"My name is {self.name}")


class kiddo(human):
    __is_cute = True

    def __init__(self, name, talks) -> None:
        super().__init__(name, talks)

    def can_talk(self):
        print("Not yet!")
