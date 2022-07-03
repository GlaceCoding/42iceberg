import sys
import yaml

class Config:
	config = None

	def __init__(self, path):
		try:
			with open(path) as file:
				config = yaml.safe_load(file)	
		except yaml.YAMLError as exc:
			print('Error in configuration file: ', exc)
			sys.exit(1)
		except FileNotFoundError as exc:
			print('Missing config file: ' + path)
			print('(?): You have to copy default.yml to local.yml')
			sys.exit(1)

		self.config = config

	def get(self):
		return self.config;
