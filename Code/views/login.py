from flask import request, render_template, session, redirect, url_for, flash
from flask.views import MethodView
from forms.login import LoginForm
from models.user import User
from utils import helper


class LoginView(MethodView):
    def get(self):
        if 'user' in session:
            return redirect(url_for('home'))

        form = LoginForm(request.form)
        context = {
            'title': 'Login',
            'form': form,
            'user': session.get('user', None)
        }

        return render_template('login.html', **context)

    def post(self):
        form = LoginForm(request.form)
        context = {
            'title': 'Login',
            'form': form,
            'user': session.get('user', None)
        }

        if form.validate():
            current_user = User.query.filter_by(email=form.email.data).first()
            if not current_user:
                flash('No user found with this email.', 'danger')

            try:
                if current_user.password == helper.create_password_hash(form.password.data):
                    flash('Sucessfully logged in!', 'warning')
                    session['user'] = {
                        'id': current_user.id,
                        'name': current_user.name,
                        'email': current_user.email
                    }
                    return redirect(url_for('home'))
                else:
                    flash(
                        'Either of the username or the password is incorrect.', 'danger')
            except:
                pass

        return render_template('login.html', **context)
