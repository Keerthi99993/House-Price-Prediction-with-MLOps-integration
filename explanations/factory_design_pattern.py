from abc import ABC,abstractmethod

#step 1: Define the Product interface
class Coffee(ABC):
    @abstractmethod
    def prepare(self):
        pass


#step 2:Implement concrete products
class Espresso(Coffee):
    def prepare(self):
        return "Preparing a rich and strong Espresso"


class Latte(Coffee):
    def prepare(self):
        return "Preparing a smooth and creamy Latte"


class Cappuccino(Coffee):
    def prepare(self):
        return "Preparing a frothy Cappuccino"


#step 3:Implement the Factory (CoffeMachine)

class CoffeeMachine:
    def make_coffee(self,coffee_type):
        if coffee_type=="Espresso":
            return Expresso().prepare()
        elif coffee_type=="Latte":
            return Latte().prepare()
        elif coffee_type=="Cappuccino":
            return Cappuccino().prepare()
        else:
            return "Unknown coffee type!!!"


#step 4:Use the factory to create products
if __name__=="__main__":
    machine=CoffeeMachine()

    coffee=machine.make_coffee("Espresso")
    print(coffee)

    coffee=machine.make_coffee("Latte")
    print(coffee)

    coffee=machine.make_coffee("Cappuccino")
    print(coffee)




    
