import gtk
from lib.graphics.graphics import Scene
from meters.bar import BarMeter
from sensors.cpu import CPUSensor
import time
import threading
class MainWindow(gtk.Window):
	def __init__(self):
		gtk.Window.__init__(self)
		gtk.gdk.threads_init()
		self.scene = Scene()
		self.bar = BarMeter({
			'y': 200,
			'vertical': True,
			'width': 2,
			'height': 200,
		}, value=0.5)
		self.cpu_sensor = CPUSensor()
		self.scene.add_child(self.bar)
		self.add(self.scene)
		self.fullscreen()
		self.show_all()
		t = threading.Thread(None, self.updater_loop)
		t.daemon = True
		t.start()

	def updater_loop(self):
		while 1:
			gtk.gdk.threads_enter()
			print 'Running animation'
			self.scene.animate(self.bar, value=(self.cpu_sensor.measure() / 100))
			gtk.gdk.threads_leave()
			time.sleep(1)

if __name__ == '__main__':
	m = MainWindow()
	gtk.main()
