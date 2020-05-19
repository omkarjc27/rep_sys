import psycopg2
from flask import Flask,request,render_template
from flask_restful import Resource,Api
from user import *
from community import *

app = Flask(__name__)
api = Api(app)

api.add_resource(ShowComm,'/community/') # GET request to get community info.
api.add_resource(CreateComm,'/community/') # PUT request to create a community. Method for internal use only.
api.add_resource(CreateUser,'/user/') # PUT request to create a user. Method for internal use only.
api.add_resource(ShowUser,'/user/<string:username>') # GET request to get user info.
api.add_resource(AddToCommunity,'/add/<string:username>') # POST request to add a user to your community. 
api.add_resource(UpVote,'/award/<string:username>') # POST request to award a user on your community.

if __name__ == '__main__':
	app.run(debug=True)
