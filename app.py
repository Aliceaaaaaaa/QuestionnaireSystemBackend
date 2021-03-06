import sys

sys.path.append('./source')
sys.path.append('./APIHandler')
sys.path.append('./ORM')

import tornado.ioloop
import tornado.web
from config import *


def load_handlers(name):
    """Load the (URL pattern, handler) tuples for each component."""
    mod = __import__(name, fromlist=['default_handlers'])
    return mod.default_handlers


class MainHandler(tornado.web.RequestHandler):
    def get(self):
        # 向响应中添加数据
        # self.write('hello,tornado,my name is get...')
        self.render('index.html')


def make_app():
    settings = {
        "cookie_secret": COOKIE_SECRET,
        "xsrf_cookies": False,
    }
    handlers = []
    handlers.extend(load_handlers('APIHandler.CheckcodeHandler'))
    handlers.extend(load_handlers('APIHandler.LoginHandler'))
    handlers.extend(load_handlers('APIHandler.RegisterHandler'))
    handlers.extend(load_handlers('APIHandler.UserInfoHandler'))
    return tornado.web.Application(handlers, **settings)


if __name__ == "__main__":
    app = make_app()
    app.listen(8888)
    tornado.ioloop.IOLoop.current().start()
