class LineReader:
	def __init__ (self, src):
		self.lines = src
		self.pos = 0
		self.name = '?'
	def __del__ (self):
		self.close ()
	def readline (self):
		try:
			r = self.lines[self.pos] #+'\n'
			self.pos = self.pos + 1
		except IndexError:
			r = None
		return r
	def close (self):
		#self.lines = None
		del self.lines
