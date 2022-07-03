from pymongo import MongoClient
from dotenv import dotenv_values

import bcrypt
import os

class Database:
	db = None

	def __init__(self):
		path = os.path.abspath('../mongodb/.env')
		print('loading ' + path)
		config = dotenv_values(path)
		user = config.get('MONGO_USER')
		pswd = config.get('MONGO_PASS')
		client = MongoClient('mongodb://' + user + ':' + pswd + '@0.0.0.0:27017/')
		try:
			client.server_info()
		except Exception as e:
			print('Cannot connect to mangodb!', e)
			exit(1)
		finally:
			print('Connected to mangodb!')
		self.db = client.db42api

		self.check_database()

	def check_database(self):
		if not 'variables' in self.db.list_collection_names():
			self.init()
		else:
			print('Database loaded')

	def init(self):
		print('Database initiated')

		self.set_variable('salt', bcrypt.gensalt())

	def get_variable(self, name):
		variable = self.db.variables.find_one({ '_id': name })
		if not variable:
			return None
		return variable['value']

	def set_variable(self, name, value):
		variables = self.db.variables

		exist = variables.find_one({ '_id': name })
		if not exist:
			variables.insert_one({
				'_id': name,
				'name': name,
				'value': value
			})
		else:
			variables.update_one({ '_id': name }, {
				'$set': {
					'name': name,
					'value': value
				}
			})
