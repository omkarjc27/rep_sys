import psycopg2
from flask import Flask,request,render_template
from flask_restful import Resource,Api
from user import *
from community import *

app = Flask(__name__)
api = Api(app)

# Methods for internal use only
api.add_resource(CreateComm,'/community/create/')
api.add_resource(CreateUser,'/user/create/')
# Methods for public use
api.add_resource(ShowComm,'/community/')
api.add_resource(AddToCommunity,'/community/add_user/')
api.add_resource(UpVote,'/user/award/')
api.add_resource(ShowUser,'/user/<string:username>')

if __name__ == '__main__':
	app.run(debug=True)