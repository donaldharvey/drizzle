import gtk
from lib.graphics.graphics import Scene
from skin import Skin
import time
import threading
from collections import deque
class MainWindow(gtk.Window):
	def __init__(self):
		gtk.Window.__init__(self)
		gtk.gdk.threads_init()
		self.scene = Scene()
		self.add(self.scene)
		self.skin = Skin('test')
		self.update_queue = deque()
		for meter in self.skin.meters.itervalues():
			self.scene.add_child(meter)
			if meter.sensor is not None:
				self.update_queue.append(meter)
		self.fullscreen()
		self.show_all()
		t = threading.Thread(None, self.updater_loop)
		t.daemon = True
		t.start()

	def updater_loop(self):
		while 1:
			for meter in self.update_queue:
				gtk.gdk.threads_enter()
				self.scene.animate(meter, value=meter.sensor.measure())
				gtk.gdk.threads_leave()
			time.sleep(1)

if __name__ == '__main__':
	m = MainWindow()
	gtk.main()
