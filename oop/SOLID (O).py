from abc import ABC, abstractmethod


class PaymentProcessor(ABC):
    @abstractmethod
    def pay(self):
        pass

class PayPal(PaymentProcessor):
    def pay(self):
        print("pay to PayPal")

class CreditCard(PaymentProcessor):
    def pay(self):
        print("pay to CreditCard")

class Crypto(PaymentProcessor):
    def pay(self):
        print("pay to Crypto")

paypal = PayPal()
creditcard = CreditCard()
crypto = Crypto()

lst = [paypal, creditcard, crypto]

for p in lst:
    p.pay()