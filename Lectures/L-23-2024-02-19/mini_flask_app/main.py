# ჩვენს შემთხვევაში მოცემული main.py ასრულებს controller-ის
# ფუნქციას.

# Importing libraries
from flask import Flask, render_template

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
    return "<h1>About</h1>"

if __name__ == "__main__":
    app.run(debug=True) # თუ ამას (debug) დავუწერ, მაშინ
    # დარეფრეშებითაც აღიქვამს ცვლილებებს.



# 2024-02-19_00-57-50