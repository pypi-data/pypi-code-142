import time

from imapclient import IMAPClient


class CraigslistEmail:
    def __init__(self, host, email, password):
        self.email = IMAPClient(host, use_uid=True, ssl=True)
        self.email.login(email, password)
        print('Connected to email inbox via IMAP')
        
    def get_unread_emails(self):
        self.email.select_folder('INBOX')
        return self.email.search(['UNSEEN', 'FROM', 'robot@craigslist.org'])

    def wait_unread_emails(self):
        print('Fetching unread emails from robot@craigslist.org')
        emails = self.get_unread_emails()
        while len(emails) == 0:
            print('No emails found, waiting 15 seconds')
            time.sleep(15)
            emails = self.get_unread_emails()
        return self.email.fetch(emails, 'RFC822').items()
    
    def delete_craigslist_emails(self):
        self.email.delete_messages(self.get_unread_emails())