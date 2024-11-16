from flask import Flask,redirect,url_for,render_template


app=Flask(__name__)

@app.route("/home")
def homepage():
    return render_template("home.html",title="home")
@app.route("/about")
def aboutpage():
    return render_template("about.html",title="about")

if __name__=="__main__":
    app.run(debug=True)