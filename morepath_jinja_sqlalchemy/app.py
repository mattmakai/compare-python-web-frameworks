import morepath
from more.jinja2 import Jinja2App


class App(Jinja2App):
    pass


@App.path(path='')
class Root(object):
    pass


@App.view(model=Root)
def hello_world(self, request):
    return "Hello world!"


@App.html(template='base.html')
def main(request):
    return {'name': 'matt'}


if __name__ == '__main__':
    config = morepath.setup()
    config.scan()
    config.commit()
    morepath.run(App())
