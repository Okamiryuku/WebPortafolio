from flask import Flask, render_template, redirect, url_for, flash, request
from flask_bootstrap import Bootstrap5


app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap5(app)


@app.route('/', methods=["GET", "POST"])
def home():
    if request.method == "POST":
        name = request.form.get('name')
        email = request.form.get('email')
        subject = request.form.get('subject')
        message = request.form.get('message')
        print(name, email, subject, message)
    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=False)
