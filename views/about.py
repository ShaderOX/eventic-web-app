from flask import render_template, session
from flask.views import MethodView


class AboutView(MethodView):
    def get(self):
        context = {
            'title': "About",
            'user': session.get('user', None)

        }
        return render_template("about.html", **context)
