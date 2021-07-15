class Log:
	def __init__(self, verbose:bool):
		self.verbose=verbose

	def info(self, message:chr): print("[Info]: " + message)
	
	def warning(self, warning:chr): print("[Warning]: " + warning)
	
	def error(self, error:chr): print("[Error]: " + error)

	def verboseinfo(self, message:chr):
		if self.verbose:
			print('''[Verbose]:''' + message)