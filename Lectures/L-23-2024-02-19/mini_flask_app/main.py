# ჩვენს შემთხვევაში მოცემული main.py ასრულებს controller-ის
# ფუნქციას.

# Importing libraries
from flask import Flask

# Creating Flask instance
app = Flask(__name__)

@app.route("/")
def home():
    return "<h1>Hello I am here</h1>"


app.run()

# 2024-02-19_00-34-18

# if __name__ == "__main__":
#     pass

