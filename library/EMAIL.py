# import necessary libraries
import smtplib, re, os
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email import encoders
from email.mime.base import MIMEBase
import email
import imaplib
import json


# to search and return data from admin 
def search(key, value, con):
	result, data = con.search(None, key, '"{}"'.format(value))
	return data


# get messages from email
def get_emails(result_bytes, con):
	msgs = [] # all the email data are pushed inside an array
	for num in result_bytes[0].split():
		typ, data = con.fetch(num, '(RFC822)')
		msgs.append(data)
	return msgs


# for access tokens
class E_mail:
	def __init__(self):
		data = json.loads(open("creden.json").read())
		self.sender_address = data['sender']
		self.sender_pass = data['pass']
		self.admin_mail = data['admin']
		self.rx = r'(?<=<div dir="auto">)([\w]+)(?=</div>)'
		self.imap_url = 'imap.gmail.com'


# Send email
class Send__E_mail(E_mail):
	# initialise object
	def __init__(self, message):
		super().__init__()
		self.subject = "PySleuth Status"  # set subject of email
		self.mail_content = message  # set text content of email

	# method to add headers to email
	def add_headers(self):
		self.message = MIMEMultipart()
		self.message['From'] = self.sender_address
		self.message['To'] = self.admin_mail
		self.message['Subject'] = self.subject

	def add_text_content(self):
		self.message.attach(MIMEText(self.mail_content, 'plain'))  # add text content

	# method to add zipfile containing user statistics
	def add_zipfile(self, filename, filepath):
		zipfile = open("data.zip", "rb")
		msg = MIMEBase('application', 'zip')
		msg.set_payload(zipfile.read())
		encoders.encode_base64(msg)
		msg.add_header('Content-Disposition', 'attachment', 
		               filename=filename)
		self.message.attach(msg)
		zipfile.close()

	def initiate_session(self):
		session = smtplib.SMTP('smtp.gmail.com', 587)
		session.starttls()
		session.login(self.sender_address, self.sender_pass)
		text = self.message.as_string()
		session.sendmail(self.sender_address, self.admin_mail, text)
		session.quit()


# Read email
class Read__E_mail(E_mail):
	def __init__(self):
		super().__init__()

	# read recent email in inbox
	def read_recent(self):
		self.con = imaplib.IMAP4_SSL(self.imap_url)
		self.con.login(self.sender_address, self.sender_pass)  # login
		self.con.select("Inbox")  # go to inbox
		msgs = get_emails(search('FROM', self.admin_mail, self.con), self.con)
		try:
			latest_msg = msgs[-1]
		except:
			return None
		data = str(latest_msg[0])
		cmd = re.findall(self.rx, data)  # filter messages from email using regex
		try:
			return cmd[0]
		except:
			return None


# clear Inbox
class Clear__E_mail(E_mail):
	def __init__(self):
		super().__init__()
		
	def clear_inbox(self):
		box = imaplib.IMAP4_SSL(self.imap_url)
		box.login(self.sender_address, self.sender_pass)
		box.select("Inbox")
		typ, data = box.search(None, 'ALL')
		for num in data[0].split():
		   box.store(num, '+FLAGS', '\\Deleted')
		box.expunge()
		box.close()
		box.logout()
