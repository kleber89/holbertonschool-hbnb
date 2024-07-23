@ns.route('/')
class UserList(Resource):
    @ns.marshal_list_with(user_model)
    def get(self):
        """List all users"""
        users = data_manager.storage['User'].values()
        return list(users)

    @ns.expect(user_model, validate=True)
    @ns.marshal_with(user_model, code=201)
    @ns.response(409, 'Email already exists', error_model)
    def post(self):
        """Create a new user"""
        data = request.json
        email = data['email']
        if any(user.email == email for user in data_manager.storage['User'].values()):
            api.abort(409, "Email already exists")

        user = User(id=len(data_manager.storage['User']) + 1,
                    email=email,
                    first_name=data['first_name'],
                    last_name=data['last_name'])
        data_manager.save(user)
        return user, 201

@ns.route('/<int:user_id>')
@ns.response(404, 'User not found', error_model)
class User(Resource):
    @ns.marshal_with(user_model)
    def get(self, user_id):
        """Fetch a user given its identifier"""
        user = data_manager.get(user_id, 'User')
        if user is None:
            api.abort(404, "User not found")
        return user

    @ns.expect(user_model, validate=True)
    @ns.marshal_with(user_model)
    @ns.response(404, 'User not found', error_model)
    def put(self, user_id):
        """Update a user given its identifier"""
        user = data_manager.get(user_id, 'User')
        if user is None:
            api.abort(404, "User not found")

        data = request.json
        user.email = data['email']
        user.first_name = data['first_name']
        user.last_name = data['last_name']
        user.updated_at = datetime.now()
        data_manager.update(user)
        return user

    @ns.response(204, 'User deleted')
    @ns.response(404, 'User not found', error_model)
    def delete(self, user_id):
        """Delete a user given its identifier"""
        user = data_manager.get(user_id, 'User')
        if user is None:
            api.abort(404, "User not found")

        data_manager.delete(user_id, 'User')
        return '', 204

if __name__ == '__main__':
    app.run(debug=True)