"""This is a module for more easily setting up code to send an email with SMTP."""

from os import environ
from smtplib import SMTP

class SendEmail:
    """Primary class for the email template module.
    Please provide the smtp server for your email service.
    IMPORTANT!!! You will need environment variables set up in the following way:
    EMAIL_ADDRESS='your email address'
    EMAIL_PASSWORD='your email password'"""
    def __init__(self, smtp_server):
        self.email = environ["EMAIL_ADDRESS"]
        self.password = environ["EMAIL_PASSWORD"]
        self.smtp = str(smtp_server)

    def send_message(self, to_email, message):
        """This method sends an email using current environment variables.
        You need to provide the recipient's email and the content of the message.
        Per the SMTP class rules, to add a subject, type 'subject:' and then do 2 new lines
        followed by the contents of the message."""
        with SMTP(self.smtp, port=587) as connection:
            connection.starttls()
            connection.login(
                self.email,
                self.password,
                )
            connection.sendmail(
                from_addr=self.email,
                to_addrs=to_email,
                msg=message,
                )
