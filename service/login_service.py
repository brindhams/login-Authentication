from flask import request
from flask import session
from models import User, Session
import uuid

class Loginservice:


    @classmethod
    def create_user(cls, user):
        name=user['name']
        mail_id = user['mail_id']
        password=user['password']
        
        User.new_user(
            name=name,
            password=password,
            mail_id=mail_id
            )

    
    @classmethod
    def login_user(cls, user):
        mail_id = user.get('mail_id')
        password = user.get('password')
        name = user.get('name')
        _user=User.get_user_by_mail_id(mail_id=mail_id)
        

        if _user.password == password:
            
            session_id = str(uuid.uuid4())
            ses = Session(
                session_id=session_id,
                mail_id=mail_id,
                name=name,
            )
            Session.create_session(ses)
            response=session_id
            return response
        else:
            return({"Message":"User Not Found"})

             
    
    @staticmethod
    def get_users():
        users = User.get_users()
        data= []
        for user in users:
            
            user_dict = dict(
                id=user.id,
                name=user.name,
                mail_id=user.mail_id,
                password=user.password
            )
            data.append(user_dict)
        return data


    

       









    
    

