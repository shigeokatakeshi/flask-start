from flask import Flask
from flask import render_template
from flask import request


app = Flask(__name__)


@app.route("/jyake/mukatsukuke")
def hello():
    return "Hello Flask"


@app.route("/hiraizumi")
def hiraizumi():
    return "やっほ"


@app.route("/user/<name>")
def heyName(name):
    return name


@app.route("/user/age/<name>/<age>")
def hayAge(name, age):
    return name + age


@app.route("/html")
def html():
    # return "<h1>Hello HTML</h1>"
    return render_template("index.html")


@app.route("/html/<name>")
def htmlName(name):
    return render_template("name.html", name=name)


@app.route("/html/age/<age>")
def htmlage(age):
    return render_template("age.html", age=age)


@app.route("/query")
def puery():

#    BBB = request.args.get("AAA")
#   return BBB
    search_text = request.args.get("search_text")
    return search_text

# http://192.168.40.96:5000/query?AAA=xxx
# http://192.168.40.96:5000/query?search_text=xxx

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
