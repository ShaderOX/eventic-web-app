from wtforms import Form, StringField, BooleanField, RadioField,  PasswordField, IntegerField, SubmitField
from wtforms.validators import *
from utils.constants import STRING_LENGTH_MAX, STRING_LENGTH_MIN, CMS_ID_LENGTH


class LoginForm(Form):
    email = StringField('Email', validators=[InputRequired("This field is required!"),
                                             Length(message=f"The length must be between {STRING_LENGTH_MIN} and {STRING_LENGTH_MAX}",
                                                    min=STRING_LENGTH_MIN,
                                                    max=STRING_LENGTH_MAX),
                                             Email("You must provide a valid Email")])
    password = PasswordField('Password', validators=[InputRequired("This field is required!"),
                                                     Length(message=f"The length must be between {STRING_LENGTH_MIN} and {STRING_LENGTH_MAX}",
                                                            min=STRING_LENGTH_MIN,
                                                            max=STRING_LENGTH_MAX)])
