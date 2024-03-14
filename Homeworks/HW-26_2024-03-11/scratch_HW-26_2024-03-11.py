# class Discount:
#   def __init__(self, customer, price):
#       self.customer = customer
#       self.price = price

#   def give_discount(self):
#       if self.customer == 'favourite':
#           return self.price * 0.2
#       if self.customer == 'vip':
#           return self.price * 0.4
      
# # Using Discount
      
# discount_favourite = Discount(price=10, customer="favourite")
# print(discount_favourite.give_discount())

# discount_favourite = Discount(price=10, customer="vip")
# print(discount_favourite.give_discount())

from abc import ABC, abstractclassmethod

class Discount(ABC):
    def __init__(self, price):
        self.price = price

    @abstractclassmethod
    def give_discount(self):
        pass


class Favourite(Discount):
    def __init__(self, price):
        super().__init__(price)
        self.customer = "favourite"

    def give_discount(self):
        return self.price * 0.2


class Vip(Discount):
    def __init__(self, price):
        super().__init__(price)
        self.customer = "vip"
    
    def give_discount(self):
        return self.price * 0.4
    
# Using Discount
    
vip_discount = Vip(price=10)
print(vip_discount.price)
print(vip_discount.give_discount())


favourite_discount = Favourite(price=10)
print(favourite_discount.price)
print(favourite_discount.give_discount())
