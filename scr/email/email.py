from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail
import os

def send_email(subject, body):
    message = Mail(
        from_email='tthu04829@gmail.com',
        to_emails='10421125@student.vgu.edu.vn',
        subject=subject,
        html_content=body)

    try:
        sg = SendGridAPIClient(os.environ.get('SENDGRID_API_KEYg'))
        response = sg.send(message)
        print(response.status_code)
        print(response.body)
        print(response.headers)
    except Exception as e:
        print(e.message)

# Example usage
send_email("Test Subject", "Hello, this is the email body.")
