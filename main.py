from flask import Flask, render_template, request
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap5(app)

# CONNECT TO DB
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///contact_form.db'
db = SQLAlchemy()
db.init_app(app)


class Contact(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    email = db.Column(db.String(100))
    subject = db.Column(db.String(100))
    message = db.Column(db.Text)


with app.app_context():
    db.create_all()


@app.route('/', methods=["GET", "POST"])
def home():
    if request.method == "POST":
        name = request.form.get('name')
        email = request.form.get('email')
        subject = request.form.get('subject')
        message = request.form.get('message')

        contact_entry = Contact(name=name, email=email, subject=subject, message=message)

        db.session.add(contact_entry)
        db.session.commit()

    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=False)
