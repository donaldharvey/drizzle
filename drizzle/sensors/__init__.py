class Sensor(object):
	defaults = {}
	def __init__(self, options={}):
		self.settings = self.defaults.copy()
		self.settings.update(options)
		
	def measure(self):
		pass
