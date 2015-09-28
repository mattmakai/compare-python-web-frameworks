# Python Web Frameworks Comparison
Have you ever wanted to see how web application code differs based on
using 
[Django](http://www.fullstackpython.com/django.html), 
[Flask](http://www.fullstackpython.com/flask.html), 
[Bottle](http://www.fullstackpython.com/bottle.html) 
or some other 
[web framework](http://www.fullstackpython.com/web-frameworks.html)? 
This repository contains the same non-trivial web app built with 
different web frameworks, 
[object-relational mappers](http://www.fullstackpython.com/object-relational-mappers-orms.html), 
form handlers and templating engines. 


## What is the web app?
The application is a contacts manager with standard create, read, update
and delete (CRUD) situations along with some 
[Twilio Voice](https://twilio.com/docs) to make the
application useful by handling conference calling and transcriptions. 


## Projects
| Name | Framework | Templates | Forms | ORM |
|------|-----------|-----------|-------|-----|
| [flask\_jinja\_sqlalchemy](https://github.com/makaimc/compare-python-web-frameworks/tree/master/flask_jinja_sqlalchemy) | [Flask](http://www.fullstackpython.com/flask.html) | Jinja | WTForms | [SQLAlchemy](http://www.fullstackpython.com/object-relational-mappers-orms.html) |
| [bottle\_jinja\_sqlalchemy](https://github.com/makaimc/compare-python-web-frameworks/tree/master/bottle_jinja_sqlalchemy) | [Bottle](http://www.fullstackpython.com/bottle.html) | Jinja | | [SQLAlchemy](http://www.fullstackpython.com/object-relational-mappers.orms.html) |
| [morepath\_jinja\_sqlalchemy](https://github.com/makaimc/compare-python-web-frameworks/tree/master/morepath_jinja_sqlalchemy) | [Morepath](http://www.fullstackpython.com/morepath.html) | Jinja | | [SQLAlchemy](http://www.fullstackpython.com/object-relational-mappers.orms.html) |
| [django\_defaults](https://github.com/makaimc/compare-python-web-frameworks/tree/master/django_defaults) | [Django](http://www.fullstackpython.com/django.html) | Django Forms | [Django ORM](http://www.fullstackpython.com/object-relational-mappers.orms.html) |


## Watch the code being written
I live stream building the apps on my
[Livecoding.tv](https://www.livecoding.tv/mattmakai) channel.

