from tornado.web import Application
from tornado.web import RequestHandler
from tornado.ioloop import IOLoop


class ChartHandler(RequestHandler):
        def get(self):
                params = self.get_arguments("user")
                if params == []:
                        self.set_status(400)
                        return self.finish("Invalid user")
                self.write('Hello ' +self.get_argument("user"))

if __name__ == "__main__":
        handler_mapping = [(r'/hello', ChartHandler),]
        application = Application(handler_mapping)
        application.listen(7777)
        IOLoop.current().start()
