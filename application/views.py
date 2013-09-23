from flask.templating import render_template
from flask.views import MethodView, View

from application import app


class HelloView(MethodView):

    def get(self):
        app.logger.debug("A call to hello view")
        return render_template("hello_world.html")

hello_view = HelloView.as_view('hello')
app.add_url_rule('/hello', view_func=hello_view, methods=['GET'])


class MainView(MethodView):
    def get(self):
        app.logger.debug("A call to main view")
        return render_template("main.html")

main_view = MainView.as_view('main')
app.add_url_rule('/main', view_func=main_view, methods=['GET'])