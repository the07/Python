class Robot:
    """Represents a robot, with a name."""

    population = 0

    def __init__(self, name):
        """Initializes the data"""
        self.name = name
        print("Initializing {}".format(self.name))

        Robot.population += 1

    def die(self):
        """I am dying"""
        print('{} is being destroyed'.format(self.name))

        Robot.population -= 1

        if Robot.population == 0:
            print('{} was the last one'.format(self.name))
        else:
            print('There are still {:d} robots working'.format(Robot.population))

    def say_hi(self):
        """Greetings by the robot"""

        print('Greetings, my name is {}'.format(self.name))

    @classmethod
    def how_many(cls):
        """Prints the current population"""
        print('We have {:d} robots.'.format(cls.population))

droid1 = Robot('R2-D2')
droid1.say_hi()
Robot.how_many()

droid2 = Robot('C-3PO')
droid2.say_hi()
Robot.how_many()

droid1.die()
droid2.die()

Robot.how_many()
print(Robot.__doc__)
print(Robot.say_hi.__doc__)
