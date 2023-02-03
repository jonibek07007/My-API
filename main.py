from flask import Flask

app = Flask(__name__)

users = [
  {
    "id": 0,
    "name": "Ali"
  },
  {
    "id": 1,
    "name": "Vali"
  }
]

@app.get('/')
def home():
	return {'message' : 'My Python API'}, 200
	
@app.get('/users')
def users_list():
	return users, 200
	
@app.get('/users/<int:id>')
def user(id):
	if 2 > id:
	    user = users[id]
	    return user
	else:
	    return {'message' : 'No User'}, 404

app.run(debug=True)