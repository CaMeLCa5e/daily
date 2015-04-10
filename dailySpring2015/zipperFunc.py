def __init__(self, config):
	# init and run db
	self.config = config
	self.db_name = config[MAIN_SECTION].get('db_file', DB_FILE)
	log.debug('use DB %s', self.db_name)
	self.profile = config[MAIN_SECTION].get('profile')
	self.memory = int(config[CLI].get('memory', None)\
		or config[self.profile].get('memory', None)
		or config[MAIN_SECTION].get('memory', None)\
		or MEMORY)
	self.provers = \
		config[CLI].get('timeout', None)\
		or config[self.profile].get('timeout', None)\
		or config[MAIN_SECTION].get('timeout', None)\
		or TIMEOUT  

	if 'tasks' in config[CLI]:
		import shelve
		log.info('Completed Tasks %s', config[CLI]['tasks'])
		s = shelve.open(config[CLI]['tasks'], writeback=True)
		self.tasks = s 
		atexit.register(lambda:s.close())
	else: 
		self.tasks = None
	self.conn = sqlite3.connect(self.db_name)
	try: 
		create_query = """#"""
		self.conn.execute(create_query)
		atexit.register(lambda : self.conn.close())
	except sqlite3.OpreationalError as e:
		pass

def raw_solve(self, provers, filenames):
	already_done = self.tasks['solved'] if self.tasks else set(())
	rows = []
	no_output = self.config[MAIN_SECTION].get('no_output', False)
	for filename in filenames:
		results = []
		print '-' *70 
		for prover_name in provers:
			if (filename, prover_name) in already_done:
				log.info('skip already executed (%s, %s)')


























