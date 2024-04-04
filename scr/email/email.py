import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Email settings
smtp_server = 'smtp.gmail.com'
smtp_port = 587
username = 'phanbaovn2003@gmail.com'
password = 'ldyfaruqafvoriar'

sender_email = username
receiver_email = '10421125@student.vgu.edu.vn'
subject = 'Test Email from Python'

# Create MIME message
message = MIMEMultipart()
message['From'] = sender_email
message['To'] = receiver_email
message['Subject'] = subject

# Email body
body = "This is a test email sent from Python. Hello World!"
message.attach(MIMEText(body, 'plain'))

# Send email
try:
    server = smtplib.SMTP(smtp_server, smtp_port)
    server.starttls()  # Secure the connection
    server.login(username, password)
    text = message.as_string()
    server.sendmail(sender_email, receiver_email, text)
    print("Email sent successfully!")
except Exception as e:
    print(f"Error: {e}")
finally:
    server.quit()
