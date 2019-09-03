import smtplib
import os
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

email = 'saocarlosagoracrawler@gmail.com'
password = os.environ.get('SCA_CRAWLER_PASS')

def send_email(emails_to_send, messageHTML):
    for email_to_send in emails_to_send:
        msg = MIMEMultipart('alternative')
        msg['From'] = email
        msg['To'] = email_to_send
        msg['Subject'] = '[Alerta] Algumas notícias no São Carlos Agora podem ser de seu interesse!'

        msg.attach(MIMEText(messageHTML, 'html'))

        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(email, password)
        text = msg.as_string()
        server.sendmail(email, email_to_send, text)
        server.quit()
