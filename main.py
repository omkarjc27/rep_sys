import psycopg2
from flask import Flask,request,render_template
from flask_restful import Resource,Api
from user import *
from community import *

app = Flask(__name__)
api = Api(app)

api.add_resource(ShowComm,'/community/show/')
api.add_resource(AddToCommunity,'/community/add_user/')
api.add_resource(CreateComm,'/community/create/')

api.add_resource(UpVote,'/user/award/')
api.add_resource(CreateUser,'/user/create/')
api.add_resource(ShowUser,'/user/show/<string:username>')

if __name__ == '__main__':
	app.run(debug=True)
