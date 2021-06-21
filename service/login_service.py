from flask import request
from models import User

class Loginservice:
    @classmethod
    def get_users(cls):
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


    @classmethod
    def create_user(cls):
        data=request.get_json()
        name=data['name']
        mail_id = data['mail_id']
        password=data['password']
        new_user=User (name=name,password=password,mail_id=mail_id)








    
    

