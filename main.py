from flask import Flask, render_template, redirect, url_for, flash, request
from flask_bootstrap import Bootstrap5
import smtplib
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap5(app)


MY_EMAIL = os.environ.get("MY_EMAIL")
EMAIL_PASS = os.environ.get("EMAIL_PASS")


@app.route('/', methods=["GET", "POST"])
def home():
    if request.method == "POST":
        name = request.form.get('name')
        email = request.form.get('email')
        subject = request.form.get('subject')
        message = request.form.get('message')
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=MY_EMAIL, password=EMAIL_PASS)
            connection.sendmail(from_addr=MY_EMAIL,
                                to_addrs=MY_EMAIL,
                                msg=f"{subject}\n\nName: {name}.\n Email: {email} \n{message}")
    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=False)
