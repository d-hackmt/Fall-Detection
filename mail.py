import smtplib
from email.message import EmailMessage
import imghdr

Sender_Email = "projectandroidengg@gmail.com"
Reciever_Email = "isha9september@gmail.com"

Password ='9689544204'
newMessage = EmailMessage()    #creating an object of EmailMessage class
newMessage['Subject'] = "Test Email from Fall Detection" #Defining email subject
newMessage['From'] = Sender_Email  #Defining sender email
newMessage['To'] = Reciever_Email  #Defining reciever email
newMessage.set_content('Hi, Person is fallen on the floor! Please help them!') #Defining email body
with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
    
    smtp.login(Sender_Email, Password)              
    smtp.send_message(newMessage)
