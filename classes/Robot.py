class Robot:
    # attribute of class Robot, it is common.
    strength = 100
    price = '1000'
    color = 'green'
    total = 0
    steps = 1

    def __init__(self, name=None):
        # increase the count for attr total
        Robot.total += 1
        self.name = name
        self.free = False
        self.extensions = set()
        self.id = f'ID: {id(self.name)}'
        self.speed = 0

    def __repr__(self):
        return f'{self.__class__.__name__} - {self.name},id {self.id}'

    def __str__(self):
        return f' {self.__class__.__name__} -{self.name},id {self.id}'

    def __bool__(self):
        return self.free == True

    def __len__(self):
        return len(self.extensions)

    def __del__(self):
        print(f'Believe in the world..Goodbye life')
        self = None

    def __add__(self, other):
        new_robot = Robot()
        new_robot.extensions.update({*self.extensions, *other.extensions})
        return new_robot

    def __iadd__(self, other):
        self.extensions.update({*other.extensions})

    def go(self, way='ahead'):
        def go_ahead():
            print(f'Go ahead by {self.steps} step')

        print('Start to go')
        if 'ahead':
            go_ahead()
        self.speed = 1

    def action(self):
        print('eplore the world')

    def increase_speed(self):
        print('Speed increased')
        self.speed += 1
        print(f'Speed equal to {self.speed}')

    def stop(self):
        print('I am stoping')
        self.speed = 0
        print('My speed equal to 10')

    def set_name(self, new_name: str):
        setattr(self, 'default_name', getattr(self, 'name'))
        setattr(self, 'name', new_name)

    def revert_default_name(self):
        setattr(self, 'name', self.default_name)

    def add_attr(self, name_attr: str, value_attr: str):
        setattr(self, name_attr, value_attr)

    def del_attr(self, name_attr: str):
        delattr(self, name_attr)

    def check_value_attr(self, name_attr, check_value):
        if hasattr(self, name_attr):
            return getattr(self, name_attr) == check_value
        else:
            print('Attribute not found')

    def add_extension(self, extension: object):
        self.extensions.add(extension)


class WarRobot(Robot):
    strength = 200
    price = '5000'
    color = 'black'

    def go(self):
        print('Start to go fast')
        self.speed = 3

    def attack(self, enemy: Robot):
        enemy.strength -= 5
        print(f'Attack this {enemy}')
        if enemy.strength != 0:
            print(f'Strength reduce - {enemy.strength}')
        else:
            print(f'Deat robot - {enemy}')
            enemy.__del__()

    def action(self, enemy: Robot):
        self.attack(enemy)
        print(f'Was be attacked - {enemy}')