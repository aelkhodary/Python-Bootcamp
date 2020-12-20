'''
How to send email with Python and how to check our inbox for received messages.

The steps :
1- connecting to an email server
2- confirming connection
3- setting a protocol
4- logging on
5- sending the message
6- close the connection

Fortunately the built in "smtplib" library in Python
makes these steps simple function calls

Each major email provider has their own SMTP(Simple Mail Transfer Protocol)
Server
EX:
   Provider                        SMTP sever domain name
   Gmail(will need App Password)    smtp.gmail.com
   Yahoo Mail                       smtp.mail.yahoo.com
......etc

'''
#Sending Emails
import smtplib
import getpass
#onnecting to an email server
smtp_object = smtplib.SMTP('smtp.gmail.com',587)
print(smtp_object.ehlo())
# using this port means you use TLS encription not SSL
print(smtp_object.starttls())

email = input("Email : ")
password =getpass.getpass('Password please : ') # gamil app password not normal password
print(smtp_object.login(email,password))
from_address = email
to_address = email
subject ='Send Eamil with Pythom'
message ='Welcome to Python World'
msg = "Subject: "+subject+'\n'+message

smtp_object.sendmail(from_address,to_address,msg)
smtp_object.quit()
