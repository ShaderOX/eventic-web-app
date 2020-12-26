from utils.constants import CMS_ID_LENGTH, STRING_LENGTH_MAX, STRING_LENGTH_MIN
from wtforms import (BooleanField, DateField, FloatField, Form, IntegerField,
                     PasswordField, RadioField, StringField, SubmitField)
from wtforms.fields.html5 import DateField, DateTimeField, TimeField
from wtforms.validators import *
from datetime import datetime


class EventRegisterationForm(Form):
    title = StringField('Event Title', validators=[InputRequired("This field is required!"),
                                                   Length(message=f"The length must be between {STRING_LENGTH_MIN} and {STRING_LENGTH_MAX}",
                                                          min=STRING_LENGTH_MIN,
                                                          max=STRING_LENGTH_MAX)])

    head = StringField('Event Head', validators=[InputRequired("This field is required!"),
                                                 Length(message=f"The length must be between {STRING_LENGTH_MIN} and {STRING_LENGTH_MAX}",
                                                        min=STRING_LENGTH_MIN,
                                                        max=STRING_LENGTH_MAX)])

    contact = StringField('Contact No.', validators=[InputRequired("This field is required!"),
                                                     Length(message=f"The length must be between {STRING_LENGTH_MIN} and {STRING_LENGTH_MAX}",
                                                            min=STRING_LENGTH_MIN,
                                                            max=STRING_LENGTH_MAX)])

    date = DateField('Event Date', format='%Y-%m-%d', validators=[
                     InputRequired("This field is required!")])

    time_start = TimeField('Start Time', format="%H:%M", validators=[
                           InputRequired("This field is required!")])

    time_end = TimeField('End Time', format="%H:%M", validators=[
                         InputRequired("This field is required!")])

    description = StringField('Event Description (300 max)', validators=[InputRequired("This field is required!"),
                                                                         Length(message=f"The length must be between {STRING_LENGTH_MIN} and {STRING_LENGTH_MAX}",
                                                                                min=STRING_LENGTH_MIN,
                                                                                max=STRING_LENGTH_MAX)])
    event_type = RadioField('Event Type', choices=('Seminar', 'Workshop'), default='Seminar',
                            validators=[InputRequired("This field is required!")])

    is_ticketed = RadioField('Is Ticketed', choices=('Ticketed', 'Non Ticketed'), default='Ticketed',
                             validators=[InputRequired("This field is required!")])

    ticket_price = FloatField('Ticket Price')

    def validate_time_end(self, time_end):
        if time_end.data <= self.time_start.data:
            raise ValidationError(
                'The ending time can not be smaller or equal to the starting time.')

    def validate_date(self, date):
        if datetime.now().date() >= date.data:
            raise ValidationError(
                "You can't choose a date that has passed! ")

    def validate_ticket_price(self, ticket_price):
        if self.is_ticketed.data.lower() == 'ticketed':
            try:
                if float(ticket_price.data) <= 0:
                    raise ValidationError(
                        'The ticket price can not be less than or equal to zero!')
            except Exception as e:
                raise ValidationError(e)
        else:
            self.ticket_price.data = 0.0
