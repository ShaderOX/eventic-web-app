from flask import render_template, session, redirect, url_for, flash
from flask.views import MethodView


class LogoutView(MethodView):
    def get(self):
        if 'user' in session:
            session.pop('user')
            flash("You have been logged out!", 'info')
        
        return redirect(url_for('home'))