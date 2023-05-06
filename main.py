from ducks.ducks import *
from ducks.fly import *

if __name__ == '__main__':
    mallard_duck = MallardDuck()
    mallard_duck.perform_quack()
    mallard_duck.perform_fly()

    model_duck = ModelDuck()
    model_duck.perform_fly()
    model_duck.set_fly_behavior(FlyRocketPowered)
    model_duck.perform_fly()
