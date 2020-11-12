import imaplib
from ._base import BaseEmailHandler


class EmailClearer(BaseEmailHandler):
    def __init__(self, progEmail: str, adminEmail: str, pwd: str):
        super(EmailClearer, self).__init__(progEmail, adminEmail, pwd)

        self.imapUrl = "imap.gmail.com"
        self.conn = imaplib.IMAP4_SSL(self.imapUrl)

    def login(self):
        self.conn.login(self.progEmail, self.pwd)

    def clearInbox(self):
        self.conn.select("Inbox")
        _, data = self.conn.search(None, 'ALL')
        for num in data[0].split():
            self.conn.store(num, '+FLAGS', '\\Deleted')

        self.conn.expunge()
        self.conn.close()

    def logout(self):
        self.conn.logout()
