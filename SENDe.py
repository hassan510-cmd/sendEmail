import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders

sender_E = "hassanmahmoud607@gmail.com"
recevi_E = "codecliniccoo@gmail.com"
sub = "lil"
passwd_E = '0173584900'


msg = MIMEMultipart()
msg['From'] = sender_E
msg['To'] = recevi_E
msg['Subject'] = sub

body = "nene"
msg.attach(MIMEText(body, 'plain'))
# method
        # attachment = open(input(),'rb')
filename = 'dfse.json'
attachment = open(filename, 'rb')

part = MIMEBase('application', 'octet-stream')
part.set_payload((attachment).read())
encoders.encode_base64(part)
part.add_header('Content-Disposition', "attachment; filename=" + filename)

msg.attach(part)
txt = msg.as_string()
server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login(sender_E, passwd_E)
print("Connection Done !")
server.sendmail(sender_E, recevi_E, txt)
print("email has been sent !")


# 1
def sendPlainText():
    import smtplib
    sender_E = input("From : ")
    passwd_E = input("Enter you passwd : ")
    recevi_E = input("To :")
    message = input("Enter your message :")
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(sender_E, passwd_E)
    print("Done")
    server.sendmail(sender_E, recevi_E, message)
    print("email has been sent")

# 2


def sendEmailWithSubject():
    from email.mime.text import MIMEText
    from email.mime.multipart import MIMEMultipart
    msg = MIMEMultipart()
    sender_E = input("From : ")
    passwd_E = input("Enter you passwd : ")
    recevi_E = input("To :")
    sub_E = input("Enter subject name :")
    body_E = input("Enter you msg : ")
    msg['From'] = sender_E
    msg['To'] = recevi_E
    msg['Subject'] = sub_E
    msg.attach(MIMEText(body_E, 'plain'))
    txt = msg.as_string()
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(sender_E, passwd_E)
    print("Connection Done !")
    server.sendmail(sender_E, recevi_E, txt)
    print("email has been sent !")

# 3


def fullMethod():
        sender_E = input("From : ")
        passwd_E = input("Enter you passwd : ")
        recevi_E = input("To :")
        sub_E = input("Enter subject name :")
        body_E = input("Enter you msg : ")

        msg = MIMEMultipart()
        msg['From'] = sender_E
        msg['To'] = recevi_E
        msg['Subject'] = sub_E

        
        msg.attach(MIMEText(body_E, 'plain'))
        # method
        # attachment = open(input(),'rb')
        filename = 'dfse.json'
        attachment = open(filename, 'rb')

        part = MIMEBase('application', 'octet-stream')
        part.set_payload((attachment).read())
        encoders.encode_base64(part)
        part.add_header('Content-Disposition', "attachment; filename=" + filename)

        msg.attach(part)
        txt = msg.as_string()
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(sender_E, passwd_E)
        print("Connection Done !")
        server.sendmail(sender_E, recevi_E, txt)
        print("email has been sent !")
