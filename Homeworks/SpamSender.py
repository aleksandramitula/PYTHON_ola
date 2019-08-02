import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


class SpamSender(object):

    def __init__(self, sender_email, password, receiver_email, text):
        self.sender_email = sender_email
        self.password = password
        self.receiver_email = receiver_email
        self.text = text

        for email in receiver_email:
            receiver_email = email

            message = MIMEMultipart("alternative")
            message["Subject"] = "Homework 4"
            message["From"] = self.sender_email
            message["To"] = receiver_email

            content = MIMEText('<html><body><p>' + str(text) + '</p></body></html>', 'html')

            message.attach(content)

            ssl.create_default_context()
            server = smtplib.SMTP_SSL('smtp.gmail.com', 465)

            server.login(self.sender_email, self.password)
            server.sendmail(self.sender_email, receiver_email, message.as_string())
            server.quit()