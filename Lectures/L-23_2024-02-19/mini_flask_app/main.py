# ჩვენს შემთხვევაში მოცემული main.py ასრულებს controller-ის
# ფუნქციას.

# Importing libraries
from flask import Flask, render_template

from models import ProductModel # model ფაილიდან შემოგვაქვს
# ProductModel კლასი

# render_template გვაძლევს საშუალებას დავარენდეროთ HTML-ის გვერდი.

# Creating Flask instance
app = Flask(__name__)

@app.route("/")
@app.route("/home")
def home():
    # return "<h1>Hello I am here</h1>"
    # return "Hello I am here"
    return render_template("home.html")

@app.route("/about")
def about():
    # ვითომ ინფორმაცია მოგვაქვს მონაცემთა ბაზიდან
    prod_1 = ProductModel("Red Bull Zero", "0% Sugar 100% wiings", 5)
    prod_2 = ProductModel("Red Bull Energy Drink", 
                        "Vitalizes Body and Mind", 6)
    prod_3 = ProductModel("Red Bull Sugarfree",
                          "Sugarfree Wiings", 7)
    
    prod_list = [prod_1, prod_2, prod_3]
    print(prod_list)
    print("I ran")

    return render_template("about.html", products=prod_list)

    # return "<h1>About</h1>"

if __name__ == "__main__":
    app.run(debug=True) # თუ ამას (debug) დავუწერ, მაშინ
    # დარეფრეშებითაც აღიქვამს ცვლილებებს.



# 2024-02-19_00-57-50