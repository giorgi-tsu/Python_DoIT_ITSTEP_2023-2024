class Customer:
    def __init__(self, name, email):
        self.name = name
        self.email = email

    def send_mail(self, message):
        pass

    def place_order(self, order):
        pass

    def generate_invoice(self, onvoice):
        pass

    def add_feedback(self, feedback):
        pass


#correct
class Customer:
    def __init__(self, name, email):
        self.name = name
        self.email = email

    def __repr__(self):
        return self.name

class EmailService:
    def send_mail(self, customer, message):
        pass
    
customer1 = Customer("Giorgi", "giorgi.tsu@gmail.com")
print(customer1)

