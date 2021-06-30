from datetime import datetime
from flask import request,jsonify
from flask import session
from flask import make_response
from models import User, Session
from functools import wraps
import uuid
import jwt





def token_id(*args, **kwargs):
    pass

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
    
    def token_id(f):
        @wraps(f)
        def decorated(*args, **kwargs):
            token = request.args.get('token')

            if not token:
                return jsonify({'message':'Token is missing'}), 403

            try:
                user = jwt.decode(token, app.config['SECRET_KEY'])
            except:
                return jsonify({'message': 'Token is invalid'}), 403

            return f(*args, **kwargs)

        return decorated
             
    
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

    


    
    

