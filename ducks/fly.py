from abc import ABC


class FlyingBehavior(ABC):
    @staticmethod
    def fly():
        pass


class FlyWithWings(FlyingBehavior):
    @staticmethod
    def fly():
        print("I'm Flying!")


class FlyNoWaY(FlyingBehavior):
    @staticmethod
    def fly():
        print("I can't fly!")


class FlyRocketPowered(FlyingBehavior):
    @staticmethod
    def fly():
        print("I'm flying with a rocket!")
