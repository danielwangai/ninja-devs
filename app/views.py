"""
To handle API CRUD operations.
"""
from flask_restful import Resource, reqparse


class UserLogin(Resource):
    """
    To handle user login.
    """
    def __init__(self):
        """
        Define parameters for login endpoint.
        """
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument("username", type=str,
                                   help="Username required",
                                   required=True
                                   )
        self.reqparse.add_argument("password", type=str,
                                   help="Password required",
                                   required=True
                                   )

    def post(self):
        """
        To handle login
        """
        pass


class UserRegistration(Resource):
    """
    To handle user registration.
    """
    def __init__(self):
        """
        Define parameters for user registration.
        """
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument("username", type=str,
                                   help="Username required",
                                   required=True
                                   )
        self.reqparse.add_argument("password", type=str,
                                   help="Password required",
                                   required=True
                                   )

    def post(self):
        """
        To create a new user.
        """
        pass
