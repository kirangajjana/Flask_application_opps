from flask import Flask,redirect,url_for,render_template


app=Flask(__name__)

@app.route("/home")
def homepage():
    return render_template("home.html",title="home")


if __name__=="__main__":
    app.run(debug=True)