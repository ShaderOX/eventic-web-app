from config import db
from flask import render_template, request, session, redirect, url_for, flash
from flask.views import MethodView
from forms.event_registration import EventRegisterationForm
from models.event import Event
from datetime import datetime
from utils import helper


class EventRegisterationView(MethodView):
    def get(self):
        if 'user' not in session:
            flash('You need to login first to create an event!', 'info')
            return redirect(url_for('login'))

        form = EventRegisterationForm(request.form)
        context = {
            'title': 'Event Registeration',
            'form': form,
            'user': session.get('user', None)
        }
        return render_template('event_registeration.html', **context)

    def post(self):
        form = EventRegisterationForm(request.form)
        context = {
            'title': 'Event Registeration',
            'form': form,
            'user': session.get('user', None)
        }

        if form.validate():
            event = Event(
                title=form.title.data,
                head=form.head.data,
                contact=form.contact.data,
                time_start=helper.get_datetime_from_date_time(
                    form.date.data, form.time_start.data),
                time_end=helper.get_datetime_from_date_time(
                    form.date.data, form.time_end.data),
                description=form.description.data,
                event_type=Event.SEMINAR if form.event_type.data.lower(
                ) == 'seminar' else Event.WORKSHOP,
                is_ticketed=Event.TICKETED if form.is_ticketed.data.lower(
                ) == 'ticketed' else Event.NON_TICKETED,
                ticket_price=form.ticket_price.data)
            try:
                db.session.add(event)
                db.session.commit()

                flash(
                    "Congratulations you have successfully created an event!", 'warning')
                return redirect(url_for('home'))
            except Exception as e:
                flash(str(e), 'danger')

        return render_template('event_registeration.html', **context)
