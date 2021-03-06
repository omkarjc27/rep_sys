from flask_restful import Resource
from flask import request
import psycopg2
import os
import hashlib
import json

class CreateUser(Resource):
	def put(self):
		# Input
		API_data = request.get_json()
		if API_data == None:
			return "Input format Not JSON"
		# DATABASE Vars
		DATABASE_URL = os.environ['DATABASE_URL']
		conn = psycopg2.connect(DATABASE_URL, sslmode='require')
		cur = conn.cursor()
		# Create Table if not exists
		cur.execute("CREATE TABLE IF NOT EXISTS users (username TEXT NOT NULL ,product_list json NOT NULL ,mail TEXT NOT NULL);")
		# Search if username or email already exists
		cur.execute("SELECT username from users WHERE username = %s OR mail = %s",(API_data['username'],API_data['email'],))
		r = cur.fetchall()
		if len(r)>0:
			if r[0][0] == str(API_data['username']):
				return 'Username Already in Use'
			else:
				return 'Email Already in Use'
		# Add user to table
		cur.execute("INSERT INTO users (username,product_list,mail) VALUES (%s,%s,%s)",(API_data['username'],json.dumps([]),API_data['email']))

		conn.commit()
		conn.close()
		cur.close()

		return 'Successful'

class UpVote(Resource):
	def post(self,user_id):
		# Inputs
		API_KEY = request.headers['THE_API_KEY']
		if API_data == None or API_KEY == None:
			return "Input format Not JSON"
		# DATABASE Vars
		DATABASE_URL = os.environ['DATABASE_URL']
		conn = psycopg2.connect(DATABASE_URL, sslmode='require')
		cur = conn.cursor()
		# Check if Community exists or not
		hsh = str((hashlib.sha256(str(API_KEY).encode())).hexdigest())
		cur.execute("SELECT community_name,user_list from community WHERE API_KEY = %s;",(hsh,))
		r = cur.fetchall()
		if len(r)==0:
			return 'Invalid API_KEY'
		community_name = r[0][0]
		user_list = r[0][1]
		# Check if user is part of the community
		flag = False
		for user in user_list:
			if user['username'] == str(user_id):
				points = user['points']
				flag = True
				break
		if not flag:
			return 'Username not in your community'			
		# Increment User's Points
		user_list.append({'username':str(user_id),'points':points+1})
		cur.execute("UPDATE community SET user_list = %s WHERE API_KEY = %s;",(json.dumps(user_list),hsh))
		# Add to user's products
		h = h_index(user_list)
		cur.execute("SELECT product_list from users WHERE username = %s;",(user_id,))
		r = cur.fetchall()
		score_list = r[0][0]
		score_list.append({'community':community_name,'global_score':h})
		cur.execute("UPDATE users SET product_list = %s WHERE username = %s;",(json.dumps(score_list),user_id))

		conn.commit()
		conn.close()
		cur.close()

		return 'Successful'

class ShowUser(Resource):
	def get(self,username):
		DATABASE_URL = os.environ['DATABASE_URL']
		conn = psycopg2.connect(DATABASE_URL, sslmode='require')
		cur = conn.cursor()
		cur.execute("SELECT product_list from users WHERE username = %s;",(username,))
		r = cur.fetchall()
		if len(r)==0:
			return 'Invalid Username'
		compiled_list = compile_list_global(r[0][0])
		conn.commit()
		conn.close()
		cur.close()
		return compiled_list


def compile_list_global(in_list):
	ret_list = {}
	total = 0
	for l in in_list:
		if l['community'] in ret_list:
			ret_list[l['community']]+=l['global_score']
		else:
			ret_list[l['community']]=l['global_score']
		total += l['global_score']

	return {'total_score':total,'community_wise':ret_list}

def h_index(user_list):
	points_table = []
	for user in user_list:
		points_table.append(user['points'])
	points_table.sort(reverse=True)
	h_index = 1
	for point in points_table:
		if point <= h_index:
			break
		else:
			h_index+=1 
	return h_index
