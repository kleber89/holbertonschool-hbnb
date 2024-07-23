from flask import Flask, request, jsonify
from flask_restx import Api, Resource, fields
from datetime import datetime
from models.user import DataManager, User  # Ensure to import your DataManager and User class

app = Flask(__name__)
api = Api(app, version='1.0', title='User API',
          description='A simple User API',)

ns = api.namespace('users', description='User operations')

# DataManager instance
data_manager = DataManager()

# User model for documentation
user_model = api.model('User', {
    'id': fields.Integer(readOnly=True, description='The unique identifier of a user'),
    'email': fields.String(required=True, description='User email'),
    'first_name': fields.String(required=True, description='First name'),
    'last_name': fields.String(required=True, description='Last name'),
    'created_at': fields.DateTime(readOnly=True, description='Time of creation'),
    'updated_at': fields.DateTime(readOnly=True, description='Time of last update')
})

# Response model for errors
error_model = api.model('Error', {
    'message': fields.String(description='Error message')
})