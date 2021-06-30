import json
import jwt
import datetime


from flask import request,Blueprint,make_response,jsonify
from service.login_service import Loginservice

LOGIN = Blueprint(
    'login',
    __name__,
    url_prefix='/api/A5'
)

@LOGIN.route('/user', methods=['POST'])
def create_user():
    data = request.get_json()
    Loginservice.create_user(user=data)
    return json.dumps({"Message": "successfully created"})


@LOGIN.route('/getuser')
def get_users():
    user=Loginservice.get_users()
    return json.dumps({"user": user})


@LOGIN.route('/login', methods=['POST'])
def login_user():
    data = request.get_json()
    response = Loginservice.login_user(user=data) 
    return json.dumps(response)


@LOGIN.route('/token', methods= ['POST'])
def verify_user():
    auth = request.authorization
    if auth and auth.password =='password':
        token = jwt.encode({'user': auth.username,'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=30)})
        return jsonify({'token' : token.encode('UTF-8')})
        
        
    return make_response('could not verify!',401,{'www-Authenticate' :'Basic realm="Login Required"'})


        



    