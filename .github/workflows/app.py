app = Flask(_name_)
api = Api(app)

class HelloWorld(Resource):
   def get(self):
    return {'hello': 'world'}

     api.add_resource(HelloWorld, '/')

     if _name_ == '_main_':
       app.run(debug=True, host='0.0.0.0')
