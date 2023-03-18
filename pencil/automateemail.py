# import smtplib
# Sender_Email = "hrutestmail@gmail.com"
# Reciever_Email = "yaddalahrudayesh@gmail.com"
# Password ="pjstknutdzhwnqvd"

# Subject = "Test Email from Hrudayesh"
# Body = "Hi, hope you are doing fine! Stay Home! Stay Safe!"
# Message = f'Subject: {Subject}\n\n{Body}'

# with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
#     smtp.ehlo()
#     smtp.starttls()
#     smtp.ehlo()
#     smtp.login(Sender_Email, Password)
#     smtp.sendmail(Sender_Email, Reciever_Email, Message)

import smtplib
import imghdr
from email.message import EmailMessage

Sender_Email = "hrutestmail@gmail.com"
Reciever_Email = "yaddalahrudayesh@gmail.com"
Password = "pjstknutdzhwnqvd"

newMessage = EmailMessage()                         
newMessage['Subject'] = "Check out the new logo" 
newMessage['From'] = Sender_Email                   
newMessage['To'] = Reciever_Email                   
newMessage.set_content('Let me know what you think. Image attached!') 

files = ['final.png', 'promo.png']

for file in files:
    with open(file, 'rb') as f:
        image_data = f.read()
        image_type = imghdr.what(f.name)
        image_name = f.name
    newMessage.add_attachment(image_data, maintype='image', subtype=image_type, filename=image_name)

with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
    
    smtp.login(Sender_Email, Password)              
    smtp.send_message(newMessage)                   