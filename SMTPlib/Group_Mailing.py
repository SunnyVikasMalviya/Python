import smtplib

sender = input("From: ").strip()
password = input("Password: ").strip()
to_id = []
to_name = []
sub = "Simply ignore/delete this mail"
server = smtplib.SMTP('smtp.gmail.com', 587)
#ehlo() is a like hello message to start the connection 
server.ehlo()
server.starttls()
server.login(sender, password)

for x in range(3):
    to_id.append(input("To : ").strip())
    to_name.append(input("Name of the recipient : ").strip())
    header = '\n'.join(["To : %s" %to_id, "From : %s" % sender, \
                         "Subject : %s" %sub])
    message = "\nHi {}!\nYou can simply go ahead and delete this message.\n\
    I was just trying to send mails using Python.\nRegards ;)".format(to_name[x])
    body = header + message
    server.sendmail(sender, to_id[x], body)
    print("Mail to {} was successfully sent.".format(to_name[x]))

server.quit()



"""
From: vikasmalviya98@gmail.com
Password: ********
To : nikkiniharika382@gmail.com
Name of the recipient : Nikki
Mail to Nikki was successfully sent.
To : dhaliwal.gurpartap@gmail.com
Name of the recipient : Sardarji
Mail to Sardarji was successfully sent.
To : vikasmalviya98@gmail.com
Name of the recipient : Sunny
Mail to Sunny was successfully sent.
"""
