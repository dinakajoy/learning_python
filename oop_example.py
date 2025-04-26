class PlayerCharacter:
    # Class Object Attribute - For static attributes across instances
    # can be accessed using self or class name eg PlayerCharacter.membership OR self.membership
    membership = True

    # Attributes - can only be accessed using self eg self.name
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # Methods - can only be accessed using self eg self.run
    def run(self):
        return 'Running...'

    def enrol(self):
        return self.membership

player1 = PlayerCharacter('Joy', 30)
print(player1.name)
print(player1.age)
print(player1.membership)
print(player1.run())
print(player1.enrol())
