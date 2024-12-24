from abc import ABC,abstractmethod


#step 1:Define the strategy interface
class PaymentMethod(ABC):
    @abstractmethod
    def pay(self,amount):
        pass


#step 2: Implement concrete strategies
class CreditCardPayment(PaymentMethod):
    def pay(self,amount):
        return f"Paying {amount} using Credit card"


class PaypalPayment(PaymentMethod):
    def pay(self,amount):
        return f"Paying {amount} using Paypal"



class BitcoinPayment(PaymentMethod):
    def pay(self,amount):
        return f"Paying {amount} using Bitcoin"



#step 3: Implement the context
class ShoppingCart:
    def __init__(self,payment_method:PaymentMethod):
        self.payment_method=payment_method
    def checkout(self,amount):
        return self.payment_method.pay(amount)


#step 4:Use the strategy in the context

if __name__=="__main__":
    cart=ShoppingCart(CreditCardPayment())
    print(cart.checkout(100)) #paying 100

    cart=ShoppingCart(PaypalPayment())
    print(cart.checkout(200)) #paying 200

    cart=ShoppingCart(BitcoinPayment())
    print(cart.checkout(300)) #paying 300

    


