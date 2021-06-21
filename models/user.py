from models import db

class User(db.Model):
    __tablename__ = 'user'

    id = db.Column(db.Integer(),  primary_key=True)
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
    def create_user(name,mail_id,password):
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