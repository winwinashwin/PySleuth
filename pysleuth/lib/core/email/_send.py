import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

from .base import BaseEmailHandler


class EmailSender(BaseEmailHandler):
    def __init__(self, progEmail: str, adminEmail: str, pwd: str):
        super(EmailSender, self).__init__(progEmail, adminEmail, pwd)

        self.subject = "PySleuth | Status"

    def login(self):
        self.session = smtplib.SMTP('smtp.gmail.com', 587)
        self.session.starttls()
        self.session.login(self.progEmail, self.pwd)

    def addHeaders(self):
        self.message = MIMEMultipart()
        self.message["From"] = self.progEmail
        self.message["To"] = self.adminMail
        self.message["Subject"] = self.subject

    def attachPlainText(self, message: str):
        self.message.attach(MIMEText(message, 'plain'))

    def attachZipFile(self, filename, filepath):
        zipfile = open(filepath, "rb")
        msg = MIMEBase('application', 'zip')
        msg.set_payload(zipfile.read())
        encoders.encode_base64(msg)
        msg.add_header('Content-Disposition', 'attachment', filename=filename)
        self.message.attach(msg)
        zipfile.close()

    def send(self):
        text = self.message.as_string()
        self.session.sendmail(self.progEmail, self.adminMail, text)

    def logout(self):
        try:
            self.session.quit()
        except smtplib.SMTPServerDisconnected as e:
            pass
