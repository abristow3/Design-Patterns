from abc import ABC


class QuackBehavior(ABC):

    @staticmethod
    def quack():
        pass


class Quack(QuackBehavior):

    @staticmethod
    def quack():
        print("Quack!")


class MuteQuack(QuackBehavior):

    @staticmethod
    def quack():
        print("<< Silence >>")


class Squeak(QuackBehavior):

    @staticmethod
    def quack():
        print("Squeak!")
