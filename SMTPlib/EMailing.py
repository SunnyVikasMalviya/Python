#SMTP is simple message transfer protocol that is used for mailing
#The python library is smtplib, which creates a client session object
import smtplib

#First we need to create a session whose instance SMTP will encapsulate the SMTP
#connection
#We will be using gmail for sending which uses port 587 to send a mail
#For other websites, you need to get the corresponding information
session = smtplib.SMTP('smtp.gmail.com', 587)
#parameters : server location and port number

session.starttls()

session.login('sender_email_id', 'sender_email_id_password')

message = 'Kaise ho sardarji?'

session.sendmail('sender_email_id', 'receiver_email_id', message)

session.quit()
