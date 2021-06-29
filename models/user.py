import uuid
from models import db

class User(db.Model):
    __tablename__ = 'user'

    id = db.Column(db.Integer(),  primary_key=True, default=lambda: str(uuid.uuid4()))
    name = db.Column(db.String(128))
    mail_id = db.Column(db.String(128))
    password = db.Column(db.String(128))

    def __init__(
            self,
            name,
            mail_id,
            password,
    ):
        self.name = name
        self.mail_id = mail_id
        self.password = password


    @staticmethod
    def new_user(name,mail_id,password):
        user=User(
            name=name,
            mail_id=mail_id,
            password=password

        )
    
        db.session.add(user)
        db.session.commit()
        
        
    @staticmethod
    def get_users():
        users = User.query.all()
        return users

    @staticmethod
    def get_user_by_mail_id(mail_id):
        user = User.query.filter_by(mail_id=mail_id).first()
        return user

class Session(db.Model):
    __tablename__='session'
    
    session_id = db.Column(db.String(),  primary_key=True, default=lambda: str(uuid.uuid4()))
    name = db.Column(db.String(128))
    mail_id = db.Column(db.String(128))
    password = db.Column(db.String(128))
    

    @staticmethod
    def create_session(Session):
        ses = Session
        return ses
