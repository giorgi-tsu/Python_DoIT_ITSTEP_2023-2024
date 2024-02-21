# ჩვენს შემთხვევაში მოცემული main.py ასრულებს controller-ის
# ფუნქციას.

# Importing libraries
from flask import Flask

# Creating Flask instance
app = Flask(__name__)

@app.route("/")
def home():
    # return "<h1>Hello I am here</h1>"
    return "Hello I am here"

@app.route("/about")
def about():
    return "<h1>About</h1>"

# 2024-02-19_00-46-46

# This is for testing purposes.

if __name__ == "__main__":
    app.run(debug=True) # თუ ამას დავუწერ მაშინ დარეფრეშებითაც 
                    # აღიქვამს ცვლილებებს.


