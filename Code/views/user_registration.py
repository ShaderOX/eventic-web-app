from config import db
from flask import render_template, request, session, flash, redirect, url_for
from flask.views import MethodView
from forms.user_registeration import UserRegisterationForm
from models.user import User
from utils import helper


class UserRegisterationView(MethodView):
    def get(self):
        if 'user' in session:
            flash('You are already registered!', 'info')
            return redirect(url_for('home'))

        form = UserRegisterationForm(request.form)
        context = {
            'title': 'User Registeration',
            'form': form,
            'user': session.get('user', None)

        }
        return render_template('user_registeration.html', **context)

    def post(self):
        form = UserRegisterationForm(request.form)
        context = {
            'title': 'User Registeration',
            'form': form,
            'user': session.get('user', None)

        }

        if form.validate():
            user = User(name=form.name.data,
                        email=form.email.data,
                        password=helper.create_password_hash(
                            form.password.data),
                        mobile_no=form.mobile_no.data,
                        CMS_id=form.CMS_id.data,
                        gender=User.MALE if form.gender.data.lower() == "male" else User.FEMALE,
                        reg_type=User.PERSONAL if form.gender.data.lower() == "personal"
                        else User.ORGANIZATION)
            try:
                db.session.add(user)
                db.session.commit()
                flash("You have been successfully registered!", 'warning')
                return redirect(url_for('login'))
            except Exception as e:
                flash(str(e), 'danger')
        return render_template('user_registeration.html', **context)
