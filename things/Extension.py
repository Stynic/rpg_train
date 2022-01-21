from faker import Faker
from random import randrange, choice


class CanSmth:
    def say(self):
        print('I am in the CanSmth')
        print(self.__class__.__name__)


class CanThink(CanSmth):
    def __init__(self, mind=True):
        self.mind = mind

    def say(self):
        print('I am in the CanThink')
        super().say()
        print('I am in the CanThink')
        print(self.__class__.__name__)


class CanUseMagic(CanSmth):
    def __init__(self, magic=True):
        self.magic = magic
        self.mind = None

    def say(self):
        print('I am in the CanUseMagic')
        super().say()
        print('I am in the CanUseMagic')
        print(self.__class__.__name__)


class Extension(CanThink, CanUseMagic):
    types_extension = ['boot', 'hat', 'body', 'arm', 'sword', 'amulet']
    type_rerity = [{'common': 1}, {'rare': 4}, {'magical': 5}, {'mythical': 6}]

    def __init__(self, name=None, extype=None, rarity=None, power=None,
                 cost=None):
        super().__init__(mind=choice([True, False]))
        self.name = None or Faker().name()
        self.extype = None or choice(Extension.types_extension)
        self.rarity = None or choice(Extension.type_rerity)
        self.power = None or randrange(
            1000) * self.rarity[list(self.rarity)[0]]
        self.cost = None or self.power * 10 + \
                    randrange(1000) * self.rarity[list(self.rarity)[0]]
        CanUseMagic.magic = True if list(self.rarity)[0] in (
            'magical', 'mythical') else False

    def __str__(self):
        return f'{self.name.title()}' + \
               f'have \nfollowing attribute: \n' + \
               f'Type: {self.extype} \n' \
               f'Rarity: {list(self.rarity)[0]} \n' \
               f'Power: {self.power} \n' \
               f'Cost: {self.cost} \n' \
               f'Mind: {self.mind} \n' \
               f'Magical: {self.magic} \n' \


    def __repr__(self):
        return f'{self.name.title()} is {self.extype}'

    def say(self):
        print('I am in the Extension')
        super().say()
        print('I am in the Extension')
        print(self.__class__.__name__)