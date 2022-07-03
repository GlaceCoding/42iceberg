import time

import srcs.app as app

def store_documents(documents, collection):
	n = 0
	for doc in documents:
		stored = collection.find_one({ '_id': doc['id'] })
		if not stored:
			n = n + 1
			doc['_id'] = doc['id']
			collection.insert_one(doc, ordered = False)
		elif stored['updated_at'] != doc['updated_at']:
			n = n + 1
			collection.update_one({ '_id': doc['id'] }, { '$set': doc })
	return n

class Campus:
	students = None
	corrections = None

	def __init__(self):
		last_update = float(app.database.get_variable('campus_table_updated_at') or 0)

		if not last_update or last_update > time.time() + 8400:
			self.refresh_all()

	def refresh_all(self):
		self.refresh_students()
		self.refresh_corrections()

		#app.database.set_variable('campus_table_updated_at', time.time())

	def refresh_students(self):
		print('Request 42api to get all students of the current campus')

		self.students = None

		app.intra42.get_all('/v2/cursus/42/users', {'campus_id':'41','sort':'-updated_at'},
			collection = app.database.db.users,
			store = store_documents,
			force = False)

	def refresh_corrections(self):
		print('Request 42api to get all corrections of the current campus')

		self.corrections = None

		app.intra42.get_all('/v2/scale_teams', {'filter[campus_id]':'41','sort':'-updated_at'},
			collection = app.database.db.scale_teams,
			store = store_documents,
			force = False)

	def get_students(self):
		return list(app.database.db.users.find({ }))

	def get_corrections(self):
		return list(app.database.db.scale_teams.find({ }))
