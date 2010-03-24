from drizzle.meters import Meter
from drizzle.lib.graphics import graphics

class BarMeter(Meter):
	nicename = 'Bar Meter'
	defaults = {
		'foreground_colour': (0, 0, 0, 1),
		'background_colour': (1, 0, 0, 0),
		'height': 2,
		'width': 200,
		'vertical': False,
		'border-colour': (0, 0, 0, 1),
		'border-size': 0,
		'invert': False
	}
	def __init__(self, options={}, value=0.0):
		Meter.__init__(self, options, value)


	def draw(self):
		s = self.settings
		# paint bg
		self.graphics.set_color(s['background_colour'])
		self.graphics.rectangle(0, 0, s['width'], s['height'])
		self.graphics.fill()
		# now foreground
		self.graphics.set_color(s['foreground_colour'])
		if not s['vertical']:
			self.graphics.rectangle(0, 0, s['width'] * self.value, s['height'])
		else:
			self.graphics.rectangle(0, (1 - self.value) * s['height'], s['width'], self.value * s['height'])
		self.graphics.fill()
