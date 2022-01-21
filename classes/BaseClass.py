from faker import Faker
from random import randrange, choice


class BaseClasses:
    def __init__(self, name=None):
        self.name = name or Faker().name()
        self.type = 'basics'
        self.power = 0
        self.energy = 100



