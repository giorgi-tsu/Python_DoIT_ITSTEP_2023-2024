# დავალება 26

# შემსრულებელი: გიორგი ცუცქირიძე

# ეს დავალება მოგვცეს 26 ლექციაზე, რომელიც ჩატარდა 
# 2024-03-11-ში და დავალების ჩაბარების ბოლო ვადაა 2024-03-18.

#******************************************************************#

print("\n",
      "-------------------- სავარჯიშო 1 --------------------", "\n")

## სავარჯიშო 1

# მოცემულ კლასს მოარგე Single Responsibility პრინციპი და 
# შესაბამისად შეცვალე კოდი. კერძოდ, დაშალე 4 კლასად:
#  User,  Storage,  HttpConnection,  Logger

class  User:
    def __init__(self, name):
        self.name = name

    def get_name(self):
        return self.name

    def save(self):
        ...

    def send(self):
        ...

    def log(self):
        ...


# SRP პრინციპის მორგება
        
class User:
    def __init__(self, name):
        self.name = name

    def get_name(self):
        return self.name


class Storage:

    def save(self):
        ...


class HttpConnection:

    def send(self):
        ...

class Logger:

    def log(self):
        ...

#------------------------------------------------------------------#

print("\n",
      "-------------------- სავარჯიშო 2 --------------------", "\n")

## სავარჯიშო 2

# მოცემული გვაქვს Discount კლასი.
# Open-Closed პრინციპის გამოყენებით საჭიროა სწორად დავნერგოთ 
# 40%_იანი ფასდაკლების ფუნქციონალი VIP კლიენტებისთვის.

class Discount:
  def __init__(self, customer, price):
      self.customer = customer
      self.price = price

  def give_discount(self):
      if self.customer == 'favourite':
          return self.price * 0.2
      if self.customer == 'vip':
          return self.price * 0.4

from abc import ABC, abstractclassmethod

class Discount(ABC):
    def __init__(self, price):
        self.price = price

    @abstractclassmethod
    def give_discount(self):
        pass

class VIP(Discount):
    def __init__(self, price):
        super().__init__(price)
        self.customer = "VIP"
    
    def give_discount(self):
        return self.price * 0.4

#------------------------------------------------------------------#

print("\n",
      "-------------------- სავარჯიშო 3 --------------------", "\n")

## სავარჯიშო 3




#------------------------------------------------------------------#

print("\n",
      "-------------------- სავარჯიშო 3 --------------------", "\n")

## სავარჯიშო 4




#------------------------------------------------------------------#