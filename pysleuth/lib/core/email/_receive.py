import imaplib
import re

from .base import BaseEmailHandler


class EmailReceiver(BaseEmailHandler):
    REGEXP = r'<div dir="\w+">([\w]+)(?=</div>)'

    def __init__(self, progEmail: str, adminEmail: str, pwd: str):
        super(EmailReceiver, self).__init__(progEmail, adminEmail, pwd)

        self.imapUrl = "imap.gmail.com"
        self.conn = imaplib.IMAP4_SSL(self.imapUrl)

    def login(self):
        self.conn.login(self.progEmail, self.pwd)

    def readRecent(self):
        self.conn.select("Inbox")
        msgs = self._getEmails(self._search(
            'FROM', self.adminMail
        ))

        try:
            latestMsg = msgs[-1]
        except Exception as e:
            return None

        cmd = re.findall(self.REGEXP, str(latestMsg[0]))

        try:
            assert len(cmd) != 0
            return cmd[0]
        except AssertionError:
            # TODO:
            return None

    def logout(self):
        self.conn.logout()

    def _getEmails(self, resultBytes):
        msgs = list()
        for num in resultBytes[0].split():
            _, data = self.conn.fetch(num, '(RFC822)')
            msgs.append(data)
        return msgs

    def _search(self, key, value):
        _, data = self.conn.search(None, key, '"{}"'.format(value))
        return data
