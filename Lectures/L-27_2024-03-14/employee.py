class Employee:

    raise_amt = 1.05

    def __init__(self, first, last, pay):
        self.first = first 
        self.last = last
        self.pay = pay
        # self.raise_amt = 2

    @property
    def email(self):
        return f"{self.last.lower()}_{self.first.lower()}@gmail.com"

    @property
    def fullname(self):
        return f"{self.first} {self.last}"

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amt)


# employee1 = Employee("Nika", "Tsitskishvili", 10000)
# # print(employee1.email())
# print(employee1.email)
# print(employee1.fullname)

# print(employee1.pay)