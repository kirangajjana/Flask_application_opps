from flask import Flask,redirect,url_for


app=Flask(__name__)


@app.route("/")

@app.route("/home/<int:num>")
def hello(num):
    return f"<h1>you number is {num},  and the sum {num+10}</h1>"

@app.route("/welcome/<name>")
def welcomepage(name):
    return f"hello mr {name} welcome you to this page"   #synamic url is working here

@app.route("/pass/<sname>/<snum>")
def passed(sname,snum):
    return f"<h1>hey user {sname.title()} you are passed with  {snum} marks</h1>"




@app.route("/examresults/<name>/<int:num>")
def data(name,num):
    if num < 30:
        return redirect(url_for("passed",sname=name,snum=num))
    else:
        return "<h1>hello kiran gajjana hoe are you</h1>"

if __name__=="__main__":
    app.run(debug=True)