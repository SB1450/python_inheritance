import math
import string
import random
import time
import abc
from itertools import count
import builtins

import math
import string
import random
import time
import abc
from itertools import count
import builtins
class Person():
    def __init__(self, name, age, ID):
        self._name = name
        self._age = age
        self._id = ID

    def __str__(self):
        return "Name: {}, Age: {}, id: {}".format(self._name, self._age, self._id)

class Lecturer(Person):
    def __init__(self, name, age, ID, salary):
        super().__init__(name, age, ID)
        self.salary = salary
    def __str__(self):
        return "{}, {}".format(super().__str__(), self.salary)

class Student(Person):
    def __init__(self, name, age, ID):
        super().__init__(name, age, ID)

l1 = Lecturer("dave", 25, "123456789", 20000)
print(l1)
