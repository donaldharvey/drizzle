import os
SKINSDIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '../skins'))
print SKINSDIR
from yaml import safe_load as load_yaml

def load_meter_or_sensor(name):
	if 'meter' in name.lower():
		module_name = name.lower().replace('meter', '')
		module_parent = 'meters'
	else:
		module_name = name.lower().replace('sensor', '')
		module_parent = 'sensors'
	temp = __import__('drizzle' + '.' + module_parent + '.' + module_name, fromlist=[name])
	object = getattr(temp, name)
	return object


class Skin(object):
	def __init__(self, name):
		filepath = os.path.join(SKINSDIR, name, name + '.yaml')
		assert os.path.isfile(filepath), 'Skin does not exist'
		data = load_yaml(open(filepath))
		self.global_conf = data.pop('drizzle')
		self.meta = data.pop('metadata')
		self.meters = {}
		self.sensors = {}

		for name, section in data.copy().iteritems():
			# sort out sensors first, do the meters later
			if type(section.get('sensor', None)) == str and not section.get('meter', None):
				sensor_data = data.pop(name)
				sensor = load_meter_or_sensor(sensor_data.pop('sensor'))(sensor_data)
				self.sensors[name] = sensor

		for name, section in data.iteritems():
			# now for the meters!
			if type(section.get('meter', None)) == str:
				# must be a meter
				sensor = self.sensors.get(section.pop('sensor', None), None)
				meter = load_meter_or_sensor(section.pop('meter'))(section, sensor)
				self.meters[name] = meter



if __name__ == '__main__':
	s = Skin('test')

