from flask import Flask, render_template

app = Flask(__name__)

@app.route('/',methods=['GET'])
def index():
    return render_template("index.html")


@app.route('/vue',methods=['GET'])
def vue():
    return render_template("vue.html")


@app.route('/jquery',methods=['GET'])
def jquery():
    return render_template("jquery.html")

if __name__ == '__main__':
    app.run(debug = True, host='0.0.0.0')