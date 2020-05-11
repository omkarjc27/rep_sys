from flask_restful import Resource
from flask import request
import psycopg2
import os
import hashlib
import json

class CreateComm(Resource):
	def post(self):
		# Input
		API_data = request.get_json()
		if API_data == None:
			return "Input format Not JSON"
		# DATABASE Vars
		DATABASE_URL = os.environ['DATABASE_URL']
		conn = psycopg2.connect(DATABASE_URL, sslmode='require')
		cur = conn.cursor()
		# Create Table if not exists
		cur.execute("CREATE TABLE IF NOT EXISTS community (community_name TEXT NOT NULL ,API_KEY TEXT NOT NULL ,mail TEXT NOT NULL ,description TEXT NOT NULL ,user_list json NOT NULL);")
		# Search if community name or email already exists
		cur.execute("SELECT community_name from community WHERE community_name = %s OR mail = %s",(API_data['community_name'],API_data['email'],))
		r = cur.fetchall()
		if len(r)>0:
			if r[0][0] == str(API_data['community_name']):
				return 'Community Name Already in Use'
			else:
				return 'Email Already in Use'
		# Add community to table
		hsh_to_return = str((hashlib.sha256((API_data['community_name']+API_data['email']).encode())).hexdigest())
		hsh_to_store = str((hashlib.sha256((hsh_to_return).encode())).hexdigest())
		cur.execute("INSERT INTO community (community_name,API_KEY,mail,description,user_list) VALUES (%s,%s,%s,%s,%s)",(API_data['community_name'],hsh_to_store,API_data['email'],API_data['desc'],json.dumps([])))

		conn.commit()
		conn.close()
		cur.close()

		return hsh_to_return

class AddToCommunity(Resource):
	def post(self):
		# Inputs
		API_data = request.get_json()
		API_KEY = request.headers['THE_API_KEY']
		if API_data == None or API_KEY == None:
			return "Input format Not JSON"
		user_id = API_data['username']
		# DATABASE Vars
		DATABASE_URL = os.environ['DATABASE_URL']
		conn = psycopg2.connect(DATABASE_URL, sslmode='require')
		cur = conn.cursor()
		# Check if username exists or not
		cur.execute("SELECT username from users WHERE username = %s;",(user_id,))
		if len(cur.fetchall()) == 0:
			return 'Username Does Not Exist'
		# Check if Community exists or not
		hsh = str((hashlib.sha256(str(API_KEY).encode())).hexdigest())
		cur.execute("SELECT community_name,user_list from community WHERE API_KEY = %s;",(hsh,))
		r = cur.fetchall()
		if len(r)==0:
			return 'Invalid API_KEY'
		community_name = r[0][0]
		# Add user to the community
		user_list = r[0][1]
		user_list.append({'username':str(user_id),'points':0})
		cur.execute("UPDATE community SET user_list = %s WHERE API_KEY = %s;",(json.dumps(user_list),hsh))
		# Add community to the user's list
		cur.execute("SELECT product_list from users WHERE username = %s;",(user_id,))
		r = cur.fetchall()
		score_list = r[0][0]
		score_list.append({'community':community_name,'product':0})
		cur.execute("UPDATE users SET product_list = %s WHERE username = %s;",(json.dumps(score_list),user_id))

		conn.commit()
		conn.close()
		cur.close()

		return 'Successful'

class ShowComm(Resource):
	def get(self):
		API_KEY = request.headers['THE_API_KEY']
		if API_KEY == None:
			return "API_KEY not found"
		DATABASE_URL = os.environ['DATABASE_URL']
		conn = psycopg2.connect(DATABASE_URL, sslmode='require')
		cur = conn.cursor()
		hsh = str((hashlib.sha256(API_KEY.encode())).hexdigest())
		cur.execute("SELECT user_list from community WHERE API_KEY = %s;",(hsh,))
		r = cur.fetchall()
		if len(r)==0:
			return 'Invalid API_KEY'
		conn.commit()
		conn.close()
		cur.close()
		return r[0][0]