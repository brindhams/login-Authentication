from  flask  import request
from flask import session
from models import User, Session
import uuid

class Loginservice:
    
    @classmethod
    def login_user(cls):
        mail_id = request.get('mail_id')
        password = request.get('password')
        user = User.get_user_by_mail_id(mail_id=mail_id)
        

        if user.password == password:
            session[mail_id]=[mail_id]
            session_id = str(uuid.uuid4())
            ses = Session(
                session_id=session_id,
                mail_id=request.get('mail_id'),
                name=request.get('name'),
            )
            Session.create_session(ses)
            response=session_id
            return response
        else:
            return({"Message":"User Not Found"})

             
    @classmethod
    def create_user(cls):
          data=request.get_json()
          name=data['name']
          mail_id = data['mail_id']
          password=data['password']
         
          User.new_user(
              name=name,
              password=password,
              mail_id=mail_id
            )


            
    @staticmethod
    def get_users():
        users = User.get_users()
        data= []
        for user in users:
            user_dict = dict(
                name=user.name,
                mail_id=user.mail_id,
                password=user.password

            )
            data.append(user_dict)
        return data


    

       









    
    

