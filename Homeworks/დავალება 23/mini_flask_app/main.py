# ჩვენს შემთხვევაში მოცემული main.py ასრულებს controller-ის
# ფუნქციას.

# Importing libraries
from flask import Flask, render_template

from models import ProductModel 

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
    obj1 = ProductModel("Red Bull Zero", "0% Sugar", 5 )
    obj2 = ProductModel("Red Energy Drink", "Vitalizes Body and Mind", 6)
    obj3 = ProductModel("Red Bull Sugarfree", "Something", 7)
    
    obj_list = [obj1, obj2, obj3]

    return render_template("about.html", obj_list=obj_list)

    # return "<h1>About</h1>"

if __name__ == "__main__":
    app.run(debug=True) # თუ ამას (debug) დავუწერ, მაშინ
    # დარეფრეშებითაც აღიქვამს ცვლილებებს.



# 2024-02-19_00-57-50