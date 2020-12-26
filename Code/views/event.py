from flask import render_template, session, redirect, url_for, flash
from flask.views import MethodView
from models.event import Event
from utils import helper


class EventView(MethodView):
    def get(self, id):
        event = Event.query.filter_by(id=id).first()
        if not event:
            flash('No such event exists!', 'danger')
            return redirect(url_for('home'))
            
        event_obj = {
            'title': event.title,
            'head': event.head,
            'event_type': "Seminar" if event.event_type == Event.SEMINAR else "Workshop",
            'ticket_price': "Free" if event.ticket_price == 0 else f'Rs. {event.ticket_price}',
            'description': event.description,
            'date': helper.get_breif_formatted_time(event.time_start),
            'days_left':  str(helper.days_left(event.time_start)).zfill(2),
            'hours_left': str(helper.hours_left(event.time_start)).zfill(2),
            'minutes_left': str(helper.minutes_left(event.time_start)).zfill(2),
            'event_span': helper.event_span_in_hours(event.time_start, event.time_end)
        }

        context = {
            'title': 'Event',
            'event': event_obj,
            'user': session.get('user', None)
        }

        return render_template('event.html', **context)
