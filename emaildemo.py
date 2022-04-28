import os , ssl
import smtplib
from email.message import EmailMessage
import imghdr #to download multiple images
#from django.template.loader import get_template
#from jinja2 import Environment, FileSystemLoader

EMAIL_ADDRESS = 'prompt2k2@gmail.com'
EMAIL_PASSWORD = os.environ.get('g_EMAIL_PASS')
EMAIL_HOST = 'smtp.gmail.com'

contacts = ['g_EMAIL_HOST','prompt2k2@hotmail.com'] #IF sending to multple reciepient 
#env = Environment(loader=FileSystemLoader('%s/templates/' % os.path.dirname(__file__)))
msg = EmailMessage()
msg['Subject'] = 'Testing Email System'
msg['From'] = EMAIL_ADDRESS
msg['To'] = ', '.join(contacts) #'prompt2k2@hotmail.com'
msg.set_content('Did you receive this email?')

##################################################################################################################################################################
#DO NOT TAMPER WITH THIS CODE. IT'S FOR SENDING HTML OR TEMPLATE

#  msg.add_alternative("""\
#      test_incident.html
    
#      """, subtype='html')

#msg.add_alternative(env.get_template('test_incident.html'))
##################################################################################################################################################################

files = ['C:\\Users\\IT Manager\\Pictures\\Pantami.PNG', 'C:\\Users\\IT Manager\\Pictures\\internet.PNG'] #List of attached files.

#attachments =

for file in files:
    
    with open(file, 'rb') as f:   #rb is read bytes 
        file_data = f.read()
        file_type = imghdr.what(f.name) #Using this if the attachement is image
        file_name = f.name #Give the attach image name
    
    
    msg.add_attachment(file_data, maintype='image', subtype=file_type, filename=file_name) #if attachement is pdf, maintype=application and subtype=octet-stream

with smtplib.SMTP_SSL(EMAIL_HOST, 465, timeout=30) as server:
    server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
    #server.starttls(ssl.create_default_context())
    
    server.send_message(msg)
    print ('Email Sent')