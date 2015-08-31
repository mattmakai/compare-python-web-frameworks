from flask import Flask, render_template
from twilio.rest import TwilioRestClient
from flask.ext.sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config.from_pyfile('config.py')

db = SQLAlchemy(app)

client = TwilioRestClient()


old_contacts = [{'first_name': 'matt', 'last_name': 'makai',
                 'phone_number': '+12025551234'}, {'first_name': 'brent',
                 'last_name': 'schooley', 'phone_number': '+12155551234'}]


@app.route('/')
def list_contacts():
    contacts = Contact.query.all()
    return render_template('contacts.html', contacts=contacts)



class Contact(db.Model):
    __tablename__ = 'contacts'
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(100))
    last_name = db.Column(db.String(100))
    phone_number = db.Column(db.String(32))

    def __repr__(self):
        return '<Contact {0} {1}: {2}>'.format(first_name, last_name,
                                               phone_number)


if __name__ == "__main__":
    app.run("0.0.0.0", port=5000, debug=True)
