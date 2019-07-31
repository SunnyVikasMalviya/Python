#SMTP is simple message transfer protocol that is used for mailing
#The python library is smtplib, which creates a client session object
import smtplib

#First we need to create a session whose instance SMTP will encapsulate the SMTP
#connection
#We will be using gmail for sending which uses port 587 to send a mail
#For other websites, you need to get the corresponding information
#This is equivalent to opening the gmail login webpage
session = smtplib.SMTP('smtp.gmail.com', 587)
#parameters : server location and port number

#TLS : transport layer security
#After creating a session, we starttls() to enable the security layer protocol
session.starttls()

#Now login into a gmail id using a valid password
session.login('sender_email_id', 'sender_email_id_password')

#This is the mail that you wish to send
message = 'Kaise ho sardarji?'

#sendmail() takes the sender_id, receiver_id and the messages as the parameters
#and sends the required mail to the id
session.sendmail('sender_email_id', 'receiver_email_id', message)

#Ending the session
#Ending the session automatically logs you out of the sender_email_id
session.quit()


#NOTE
"""
Google blocks sign-in attempts from apps which do not use modern security
standards (mentioned on their support page). You can however, turn on/off
this safety feature by going to the link below:

Go to this link and select Turn On
https://www.google.com/settings/security/lesssecureapps
"""
