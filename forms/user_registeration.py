from utils.constants import CMS_ID_LENGTH, STRING_LENGTH_MAX, STRING_LENGTH_MIN
from wtforms import (BooleanField, DateField, Form, IntegerField,
                     PasswordField, RadioField, StringField, SubmitField,
                     TextAreaField, TimeField)
from wtforms.validators import *


class UserRegisterationForm(Form):
    reg_type = RadioField('Gender', choices=('Personal', 'Organization'), default='Personal',
                          validators=[InputRequired("This field is required!")])

    name = StringField('Name', validators=[InputRequired("This field is required!"),
                                           Length(message=f"The length must be between {STRING_LENGTH_MIN} and {STRING_LENGTH_MAX} characters. ",
                                                  min=STRING_LENGTH_MIN,
                                                  max=STRING_LENGTH_MAX)])

    email = StringField('Email', validators=[InputRequired("This field is required!"),
                                             Length(message=f"The length must be between {STRING_LENGTH_MIN} and {STRING_LENGTH_MAX} characters. ",
                                                    min=STRING_LENGTH_MIN,
                                                    max=STRING_LENGTH_MAX),
                                             Email("You must provide a valid Email. ")])
    password = PasswordField('Password', validators=[InputRequired("This field is required!"),
                                                     Length(message=f"The length must be between {STRING_LENGTH_MIN} and {STRING_LENGTH_MAX} characters. ",
                                                            min=STRING_LENGTH_MIN,
                                                            max=STRING_LENGTH_MAX)])
    mobile_no = StringField('Mobile No.', validators=[InputRequired("This field is required!"),
                                                      Length(message=f"The length must be between {STRING_LENGTH_MIN} and {STRING_LENGTH_MAX} characters. ",
                                                             min=STRING_LENGTH_MIN,
                                                             max=STRING_LENGTH_MAX)])
    CMS_id = StringField('6 Digit CMS ID', validators=[InputRequired("This field is required!"),
                                                       Length(message=f"The length must be {CMS_ID_LENGTH} characters long.",
                                                              min=CMS_ID_LENGTH,
                                                              max=CMS_ID_LENGTH)])
    gender = RadioField('Gender', choices=('Male', 'Female'), default='Male',
                        validators=[InputRequired("This field is required!")])

    def validate_CMS_id(self, obj):
        try:
            if len(obj.data) == CMS_ID_LENGTH:
                int(obj.data)
            else:
                raise Exception()
        except:
            raise ValidationError("This is an invalid CMS ID.")

