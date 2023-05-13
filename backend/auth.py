"""
AUTH:: handles Sigup Login
"""

from flask_restx import Resource, Namespace, fields
from flask import request, jsonify, make_response
from dbmodels import Userdata
from flask_jwt_extended import create_access_token, create_refresh_token, jwt_required , get_jwt_identity
from werkzeug.security import generate_password_hash, check_password_hash 

auth_ns = Namespace('auth', description="A namespace for our Authentication")

"""
     Sigin Up
"""

signup_model = auth_ns.model(
    "SiginUP",
    {
        "username": fields.String(),
        "email": fields.String(),
        "password": fields.String()
    }
)

@auth_ns.route('/signup')
class Signup(Resource):

    @auth_ns.expect(signup_model)
    def post(self):
        """
        Siginup , creating a new user
        """   
        data = request.get_json()
         # user id is hex cause why not
        username = data.get('username')

        db_user = Userdata.query.filter_by(username = username).first()

        if db_user is not None:
            return jsonify({"message":f"User with username {username} already exists"}, {"data" : f"{db_user}"})

        new_user = Userdata(
            username = data.get('username'),
            email = data.get('email'),
            password = generate_password_hash(data.get('password'))
        )
        new_user.save()
        return jsonify({"message": "User Created Succesfully"})
    
"""
Login
"""

login_model = auth_ns.model(
    "Login",
    {
        'username':fields.String(),
        'password':fields.String()
    }
)



@auth_ns.route('/login')
class Login(Resource):
    """Login, a user"""
    @auth_ns.expect(login_model)
    def post(self):
        data = request.get_json()

        username = data.get('username')
        password = data.get('password')

        #check and validate
        db_user = Userdata.query.filter_by(username= username).first()

        if db_user and check_password_hash(db_user.password, password):
            access_token = create_access_token(identity = db_user.username)
            refresh_token = create_refresh_token(identity = db_user.username)

            return jsonify(
                {
                    "access token" : access_token,
                    "refresh_token" : refresh_token,
                    "username": db_user.username
                 }
            )

@auth_ns.route('/refresh')
class RefreshResourse(Resource):
    @jwt_required(refresh = True)
    def post(self):
        """Access Current login User"""
        current_user = get_jwt_identity()
        new_access_token = create_access_token(identity=current_user)
        return make_response(jsonify({"access_token":f"{new_access_token}"}), 200)