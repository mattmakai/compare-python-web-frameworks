from flask import Flask, render_template, redirect, url_for, Response
from twilio.rest import TwilioRestClient
from twilio import twiml
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.wtf import Form
from wtforms import StringField
from wtforms.validators import Required, Length

from config import TWILIO_NUMBER


app = Flask(__name__)
app.config.from_pyfile('config.py')

db = SQLAlchemy(app)

client = TwilioRestClient()


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


@app.route('/delete-contact/<int:id>')
def delete_contact(id):
    contact = Contact.query.get_or_404(id)
    db.session.delete(contact)
    db.session.commit()
    return redirect(url_for('contacts'))


@app.route('/call/<int:id>')
def call(id):
    contact = Contact.query.get_or_404(id)
    client.calls.create(to=contact.phone_number, from_=TWILIO_NUMBER,
        url="http://twimlbin.com/external/5433e2a6577fdbf5")
    return redirect(url_for('contacts'))


@app.route('/conference-twiml')
def conference_twiml():
    twiml_response = twiml.Response()
    twiml_response.dial().conference('pycontacts')
    return Response(str(twiml_response))


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
