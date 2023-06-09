# Step 1: Importing the required libraries
# Step 2: Initialize the flask lib
# Step 3: Routing to the pages
# Step 4: Running the application

from flask import Flask

app = Flask(__name__)

@app.route('/')
def demo():
    return "Hello all welcome to vit"


if __name__ == '__main__':
    app.run()