from hashlib import sha256
from datetime import datetime


def create_password_hash(password: str):
    return sha256(password.encode()).hexdigest()


def get_datetime_from_date_time(date, time):
    return datetime(
        year=date.year,
        month=date.month,
        day=date.day,
        hour=time.hour,
        minute=time.minute,
        second=time.second,
        microsecond=time.microsecond,
        tzinfo=time.tzinfo,
        fold=time.fold)


def days_left(datetime_object):
    date_delta = datetime_object.date() - datetime.now().date()
    return abs(date_delta.days)


def hours_left(datetime_object):
    date_delta = datetime_object.hour - datetime.now().hour
    return abs(date_delta)


def minutes_left(datetime_object):
    date_delta = datetime_object.minute - datetime.now().minute
    return abs(date_delta)


def event_span_in_hours(time_start, time_end):
    start = datetime.strftime(time_start, "%I %p")
    end = datetime.strftime(time_end, "%I %p")
    return f"{start} - {end}"


def get_breif_formatted_time(datetime_object):
    return datetime_object.strftime("%b %d, %Y")
