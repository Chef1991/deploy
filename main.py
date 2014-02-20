#!/usr/bin/python

import args
from config import Config
from config import ConfigError

batch_file_name  = ".deploy_batch"
	
def handle_config_error(e):
	if e.cause is ConfigError.INVALID_NAME_ERROR:
		print "the supplied name is not valid."
	elif e.cause is ConfigError.NO_NAME_ERROR:
		print "A destination name is required."
	elif e.cause is ConfigError.JSON_ERROR:
		print "Config file is not properly formatted."
	exit()


def main():
	dest = args.get_destination()
	init = args.get_init()
	config = Config()
	if init:
		if config.config_file_exists():		#check if the stuff already exists and handle the stuff
			print "config file already exists"
			exit()
		else:
			config.create_config_template()
			print "Config file created"
			exit()
	else:
											# go to config and check if file exists, 
		if config.config_file_exists():		# if it does try to use it, show help if
			try:
				config.load_config(dest)	# error occurs
			except ConfigError, e:
				handle_config_error(e)
				
		else:
			print "No Config file found, use 'deploy --init' to create a sample config file."
			exit()

	# everthing is set up i think,
	# implement sftp here

if __name__ == '__main__':
	main()







