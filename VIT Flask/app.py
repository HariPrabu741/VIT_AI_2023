from flask import Flask,render_template,request

app = Flask(__name__)

@app.route('/')
def demo():
    return render_template('log.html')
@app.route('/login',methods=['POST'])
def log():
    user=request.form['name']
    password=request.form['pas']
    op = [user, password]

    print(op)
    return render_template('log.html',output=op)

if __name__ == '__main__':
    app.run()