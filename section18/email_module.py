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

print('\n***************** Sending Emails *******************')
import smtplib
import getpass
'''
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
subject ='Send Eamil with Python'
message ='Welcome to Python World'
msg = "Subject: "+subject+'\n'+message

smtp_object.sendmail(from_address,to_address,msg)
smtp_object.quit()

'''

print('\n***************** Received Emails *******************')
'''
* Built in "imaplib" and email libraries in Python
* The imaplib library has a special syntax for searching your inbox
'''
print('\n***************** Viewing Emails *******************')
import imaplib
M = imaplib.IMAP4_SSL('imap.gmail.com')
email = input("Email : ")
password = getpass.getpass('Password please : ')
M.login(email,password)
print(M.list())
M.select('inbox')
typ , data = M.search(None , 'SUBJECT "Send Eamil with Pythom"')
print(typ)
print(data)
email_id = data[0]
result , email_data = M.fetch(email_id,'(RFC822)')
print(result)
print(email_data)
raw_email = email_data[0][1]
raw_email_string = raw_email.decode('utf-8')
print(f'\n Email detail is :: {raw_email_string}')
import email
email_message = email.message_from_string(raw_email_string)
for part in email_message.walk():
    if part.get_content_type() == 'text/plain':
        body = part.get_payload(decode=True)
        print(body)
