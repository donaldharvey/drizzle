from drizzle.lib.graphics import graphics
universal_defaults = {
	'x': 10,
	'y': 10,
}
class Meter(graphics.Sprite):
	nicename = 'Meter'
	defaults = {}

	def __init__(self, settings, sensor=None, value=0.0):
		self.value = value
		self.sensor = sensor
		self.settings = universal_defaults.copy()
		self.settings.update(self.defaults)
		self.settings.update(settings)
		print self.settings
		self.s = self.settings # shorthand
		s = self.settings
		graphics.Sprite.__init__(self, s['x'], s['y'])
		self.draw()

	def draw(self):
		pass

	def _draw(self, *args, **kwargs):
		graphics.Sprite._draw(self, *args, **kwargs)
		self.draw()

	def update_value(self, new_value):
		if self.value != new_value:
			self.value = new_value
			self.draw()
