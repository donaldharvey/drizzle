from drizzle.sensors import Sensor
import re
import linecache

class RAMSensor(Sensor):
	defaults = {}

	def __init__(self, options={}):
		Sensor.__init__(self, options)
		# find out the location in the file of various bits of info about RAM
		# as defined at http://git.kernel.org/?p=linux/kernel/git/torvalds/linux-2.6.git;a=blob;f=Documentation/filesystems/proc.txt;hb=HEAD
		self.data_positions = {}
		contents = open('/proc/meminfo').read()
		contents = contents.split('\n')[:-1]
		for index, line in enumerate(contents):
			print line
			print line.split()
			try:
				self.data_positions[line.split()[0][:-1]] = index + 1 # line numbers aren't zero-based
			except IndexError:
				pass # in case line is empty


	def _get_data(self, name):
		linecache.checkcache('/proc/meminfo')
		line = linecache.getline('/proc/meminfo', self.data_positions[name])
		data = int(line.split()[1])
		return data

	def measure(self):
		# calc percentage of RAM use
		l = self.data_positions # makes the following a bit easier to write
		total_mem = self._get_data('MemTotal') - self._get_data('Buffers')
		free_mem = self._get_data('MemFree') + self._get_data('Cached')
		percent_used = round(1 - (float(free_mem) / float(total_mem)), 4)
		return percent_used



if __name__ == '__main__':
	s = RAMSensor()
	while 1:
		print s.measure()
		import time
		time.sleep(1)