from flask import Flask, render_template, redirect
from twilio.rest import TwilioRestClient
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.wtf import Form
from wtforms import StringField
from wtforms.validators import Required, Length


app = Flask(__name__)
app.config.from_pyfile('config.py')

db = SQLAlchemy(app)

client = TwilioRestClient()


old_contacts = [{'first_name': 'matt', 'last_name': 'makai',
                 'phone_number': '+12025551234'}, {'first_name': 'brent',
                 'last_name': 'schooley', 'phone_number': '+12155551234'}]


@app.route('/', methods=['GET', 'POST'])
def contacts():
    form = ContactForm()
    if form.validate_on_submit():
        contact = Contact()
        form.populate_obj(contact)
        db.session.add(contact)
        db.session.commit()
        return redirect(url_for('contacts'))
    contacts = Contact.query.all()
    return render_template('contacts.html', contacts=contacts, form=form)



class Contact(db.Model):
    __tablename__ = 'contacts'
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(100))
    last_name = db.Column(db.String(100))
    phone_number = db.Column(db.String(32))

    def __repr__(self):
        return '<Contact {0} {1}: {2}>'.format(first_name, last_name,
                                               phone_number)


class ContactForm(Form):
    first_name = StringField('First Name', validators=[Required(),
                             Length(1, 100)])
    last_name = StringField('Last Name', validators=[Required(),
                            Length(1, 100)])
    phone_number = StringField('Phone Number', validators=[Required(),
                               Length(1, 32)])


if __name__ == "__main__":
    app.run("0.0.0.0", port=5000, debug=True)
