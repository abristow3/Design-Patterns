from abc import ABC
from ducks.fly import *
from ducks.quack import *


class Duck(ABC):

    def __init__(self):
        self.fly_behavior = FlyingBehavior()
        self.quack_behavior = QuackBehavior()

    @staticmethod
    def display():
        pass

    def perform_fly(self):
        self.fly_behavior.fly()

    def perform_quack(self):
        self.quack_behavior.quack()

    def set_fly_behavior(self, fb):
        self.fly_behavior = fb

    def set_quack_behavior(self, qb):
        self.quack_behavior = qb

    @staticmethod
    def swim():
        print("All ducks float even decoys!")


class MallardDuck(Duck):
    def __init__(self):
        super().__init__()
        self.quack_behavior = Quack
        self.fly_behavior = FlyWithWings

    @staticmethod
    def display():
        print("I'm a real Mallard Duck!")


class ModelDuck(Duck):
    def __init__(self):
        super().__init__()
        self.quack_behavior = Quack
        self.fly_behavior = FlyNoWaY

    @staticmethod
    def display():
        print("I'm a real Model Duck!")
