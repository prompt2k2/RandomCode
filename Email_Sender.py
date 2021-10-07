import smtplib
import os
from email.message import EmailMessage

g_EMAIL_ADDRESS = os.environ.get('g_EMAIL_USER')
g_EMAIL_PASSWORD = os.environ.get('g_EMAIL_PASS')

msg = EmailMessage()
msg['Subject'] = 'Check Image I'
msg['From'] = g_EMAIL_ADDRESS
msg['TO'] = 'prompt2k2@gmail.com'
msg.set_content('Testing Python delivery of email, see image')


with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
       
    smtp.login(g_EMAIL_ADDRESS, g_EMAIL_PASSWORD) #if MFA is activate EMAIL_PASSWORD is the APP password created through gmail
        
    smtp.send_message(msg)