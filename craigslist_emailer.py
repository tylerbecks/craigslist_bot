import smtplib

class SendEmail(object):

    def __init__(self):
        self.from_addr = 'tylerbecksslack@gmail.com'
        self.login = 'tylerbecksslack@gmail.com'
        self.password = 'cqyQoi5yGYNVzPMR70l2YDBERKsx6e'
        self.smtpserver='smtp.gmail.com:587'

    def send_email(self, to_addr, subject, message):
        try:
            header = 'From: %s\n' % self.from_addr
            header += 'To: %s\n' % to_addr
            header += 'Subject: %s\n\n' % subject
            message = header + message

            server = smtplib.SMTP(self.smtpserver)
            server.starttls()
            server.login(self.login, self.password)
            response = server.sendmail(self.from_addr, to_addr, message)
            return response
            server.quit()

        except Exception as e:
            print(e)
            return

    def generate_message(self, item_type, url):
        return  """
            Hey,

            I'm interested in your {item_type}.  Is it still available?  And why are you selling it?

            Thanks!
            Tyler

            {url}
            """.format(item_type=item_type, url=url)
