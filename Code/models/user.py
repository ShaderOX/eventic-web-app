from config import db
from utils.constants import HASHED_PASSWORD_LENGTH, STRING_LENGTH_MAX, CMS_ID_LENGTH


class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(STRING_LENGTH_MAX),
                     unique=False,
                     nullable=False)
    email = db.Column(db.String(STRING_LENGTH_MAX),
                      unique=True,
                      nullable=False)
    password = db.Column(db.String(HASHED_PASSWORD_LENGTH),
                         unique=False,
                         nullable=False)
    mobile_no = db.Column(db.String(STRING_LENGTH_MAX),
                          unique=False,
                          nullable=False)
    CMS_id = db.Column(db.String(CMS_ID_LENGTH),
                       unique=True,
                       nullable=False)

    MALE = True
    FEMALE = True
    gender = db.Column(db.Boolean, unique=False, nullable=False)

    PERSONAL = 1
    ORGANIZATION = 0
    reg_type = db.Column(db.Boolean, unique=False, nullable=False)

    def __repr__(self):
        return f"<{self.id}. {self.name} - {self.CMS_id}>"
