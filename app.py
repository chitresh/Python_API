from flask import Flask
from flask_restful import Api, Resource, reqparse

app = Flask(__name__)
api = Api(app)

users = [
	{	
	"name": "Nicholas",
	"age":"42",
	"occupation" : "NW Engineer"
	},
	{	
	"name": "Elvin",
	"age":"22",
	"occupation" : "Doctor"
	},
	{	
	"name": "Jass",
	"age":"52",
	"occupation" : "Web Developer"
	}
	]
	
class User(Resource): 
	def get(self, name): 
		for user in users:
			if(name == user["name"]):
				return user, 200
		return "User not found", 404
		
	def post(self, name):
		parser = reqparse.RequestParser()
		parser.add_argument("age")
		parser.add_argument("occupation")
		args = parser.parse_args()
		
		for user in users:
			if(name == user["name"]):
				return "User with name {} already exists".format(name), 400
				
		user = {
			"name": name,
			"age": args["age"],
			"occupation": args["occupation"]
			}
			
		users.append(user)
		return user, 201
		
	def put(self,name):
		parser = reqparse.RequestParser()
		parser.add_argument("age")
		parser.add_argument("occupation")
		args = parser.parse_args()
		
		for user in users:
			if(name == user["name"]):
				user["age"] = args["age"]
				user["occupation"]= args["occupation"]
				return user, 200
				
		user = {
				"name" : name,
				"age" : args["age"],
				"occupation" : args["occupation"]
		}
			
		users.append(user)
		return user, 201
		
		
		api.add_resource(user, "/user/<string:name>")
		app.run(debug=True)
	

	
