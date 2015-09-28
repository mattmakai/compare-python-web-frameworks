import os

from bottle import (install, route, run, jinja2_template as template,
                    post, redirect, request, static_file, TEMPLATE_PATH,)
from bottle.ext import sqlalchemy
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from twilio.rest import TwilioRestClient


SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL', None)
TWILIO_NUMBER = os.environ.get('TWILIO_NUMBER', None)

TEMPLATE_PATH.append("./templates")

Base = declarative_base()
engine = create_engine(SQLALCHEMY_DATABASE_URI, echo=True)

sqlalchemy_plugin = sqlalchemy.Plugin(
    engine,
    Base.metadata,
    keyword='db',
    create=False,
    commit=True,
    use_kwargs=False
)

install(sqlalchemy_plugin)

client = TwilioRestClient()


@route('/')
def index(db):
    contacts = db.query(Contact).all()
    return template('contacts.html', contacts=contacts, form=None)


@post('/')
def new_contact(db):
    first_name = request.forms.get('first_name', None)
    last_name = request.forms.get('last_name', None)
    phone_number = request.forms.get('phone_number', None)
    if _validate_contact_data(first_name, last_name, phone_number):
        _save_contact(db, first_name, last_name, phone_number)
    return redirect('/')


def _validate_contact_data(first_name, last_name, phone_number):
    if not (first_name and len(first_name) > 0 and len(first_name) <= 100):
        return False
    if not (last_name and len(last_name) > 0 and len(last_name) <= 100):
        return False
    if not (phone_number and len(phone_number) > 0 and
            len(phone_number) <= 32):
        return False
    return True

def _save_contact(db, first_name, last_name, phone_number):
    contact = Contact()
    contact.first_name = first_name
    contact.last_name = last_name
    contact.phone_number = phone_number
    db.add(contact)


@route('/delete/<id>')
def delete(id, db):
    contact = db.query(Contact).get(id)
    if contact is None:
        return 'error'
    db.delete(contact)
    db.commit()
    return redirect('/')


@route('/call/<id>')
def call(id, db):
    contact = db.query(Contact).get(id)
    if contact is None:
        return 'error'
    client.calls.create(to=contact.phone_number, from_=TWILIO_NUMBER,
        url="http://twimlbin.com/external/5433e2a6577fdbf5")
    return redirect('/')


@route('/conference-twiml')
def conference_twiml():
    twiml_response = twiml.Response()
    twiml_response.dial().conference('pycontacts')
    return Response(str(twiml_response))



@route('/static/css/<filename>')
def server_static_css(filename):
    return static_file(filename, root='./static/css')


@route('/static/js/<filename>')
def server_static_css(filename):
    return static_file(filename, root='./static/js')


class Contact(Base):
    __tablename__ = 'contacts'
    id = Column(Integer, primary_key=True)
    first_name = Column(String(100))
    last_name = Column(String(100))
    phone_number = Column(String(32))

    def __repr__(self):
        return '<Contact {0} {1}: {2}>'.format(self.first_name,
                                               self.last_name,
                                               self.phone_number)


if __name__ == '__main__':
    port = int(os.environ.get('PORT', 8080))
    run(host='0.0.0.0', port=port, debug=True, reloader=True)


