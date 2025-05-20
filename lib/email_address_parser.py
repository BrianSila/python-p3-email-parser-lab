class EmailAddressParser():

    def __init__(self, emails):
        self.emails = emails

    def parse(self):
        emails = self.emails.replace(',', ' ').split()
        
        valid_emails = [
            email for email in emails 
            if '@' in email and 
               '.' in email and
               email.count('@') == 1 and
               email.index('@') < email.rindex('.')
        ]
        return sorted(list(set(valid_emails)))