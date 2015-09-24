import os

from bottle import (install, route, run, jinja2_template as template,
                    redirect, static_file, TEMPLATE_PATH,)
from bottle.ext import sqlalchemy
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base


SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL', None)
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


@route('/')
def index(db):
    contacts = db.query(Contact).all()
    return template('contacts.html', contacts=contacts, form=None)


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
    pass


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


