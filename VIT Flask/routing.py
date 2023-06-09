from flask import Flask

app = Flask(__name__)

@app.route('/vit')
def demo():
    return "Hello all welcome to vit"

@app.route('/ai')
def demo1():
    return "Hello all welcome to AI"

if __name__ == '__main__':
    app.run()