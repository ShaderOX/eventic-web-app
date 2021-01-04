from config import db
from utils.constants import STRING_LENGTH_MAX, EVENT_DESCRIPTION_LENGTH


class Event(db.Model):
    __tablename__ = 'events'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(STRING_LENGTH_MAX),
                      unique=False, nullable=False)
    head = db.Column(db.String(STRING_LENGTH_MAX),
                     unique=False, nullable=False)
    contact = db.Column(db.String(STRING_LENGTH_MAX),
                        unique=False, nullable=False)

    time_start = db.Column(db.DateTime, unique=False, nullable=False)
    time_end = db.Column(db.DateTime, unique=False, nullable=False)
    description = db.Column(
        db.String(EVENT_DESCRIPTION_LENGTH), unique=False, nullable=False)

    WORKSHOP = True
    SEMINAR = False
    event_type = db.Column(db.Boolean,  unique=False, nullable=False)

    TICKETED = True
    NON_TICKETED = False
    is_ticketed = db.Column(db.Boolean, unique=False, nullable=False)

    ticket_price = db.Column(db.Float,
                             nullable=True, unique=False,
                             default=0.0)

    def __repr__(self):
        return f"<{self.id}. {self.title} - {self.head}>"
