from drizzle.sensors import Sensor
import re

class CPUSensor(Sensor):
	defaults = {}
	def __init__(self, options={}):
		Sensor.__init__(self, options)
		self.re = re.compile('^cpu .*\n')
		self.prev_idle = 0
		self.prev_total = 0

	def measure(self):

		f = open('/proc/stat')
		contents = f.read()
		f.close()
		cpu = self.re.search(contents).group(0)[5:].split(' ')
		idle = int(cpu[3])
		total = 0
		for c in cpu:
			total += int(c)
		diff_idle = idle - self.prev_idle
		diff_total = total - self.prev_total
		usage = round(float((diff_total - diff_idle)) / diff_total, 4)
		self.prev_total = total
		self.prev_idle = idle
		return usage


if __name__ == '__main__':
	s = CPUSensor()
	while 1:
		print s.measure()
		import time
		time.sleep(1)