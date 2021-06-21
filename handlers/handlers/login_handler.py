import json

from flask import request,Blueprint
from service.login_service import Loginservice

LOGIN = Blueprint(
    'login',
    __name__,
    url_prefix='/api/A5'
)

@LOGIN.route('/user',methods=['POST'])
def create_user():
    data = request.get_json()
    Loginservice.create_user()
    return json.dumps({"Message": "successfully created"})


@LOGIN.route('/getuser')
def get_users():
    user=Loginservice.get_users()
    return json.dumps({"user": user})

