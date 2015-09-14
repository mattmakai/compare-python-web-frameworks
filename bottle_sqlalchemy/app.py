import os
from bottle import route, run, template



@route('/')
def index():
    return template('This is a template {{ stub }}.', stub="stub.")


@route('/name/<name>')
def name(name):
    return template(index_html, author=name)


if __name__ == '__main__':
    port = int(os.environ.get('PORT', 8080))
    run(host='0.0.0.0', port=port, debug=True, reloader=True)

