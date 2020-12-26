from flask import render_template, session, flash
from flask.views import MethodView
from models.event import Event
from utils import helper


class HomeView(MethodView):
    def get(self):
        events = []
        for event in Event.query.order_by(Event.time_start).all():
            events.append({
                'id': event.id,
                'title': event.title,
                'date': helper.get_breif_formatted_time(event.time_start),
                'type': "Seminar" if event.event_type == Event.SEMINAR else "Workshop",
                'is_ticketed': (f"Rs. {event.ticket_price}" if event.is_ticketed else "Free"),
                'head': event.head
            })

        context = {
            'title': "Home",
            'user': session.get('user', None),
            'events': events
        }
        return render_template("home.html", **context)
