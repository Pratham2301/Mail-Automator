from json import encoder
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

subject_mail = "Trial"
from_mail = ''
password = ''
rec = ['','']

to_mail = ", ".join(rec)


msg = MIMEMultipart()

msg['From'] = from_mail
msg['To'] = to_mail
msg['Subject'] = subject_mail

body = '''
<html>
<head>
    <title></title>
</head>
<style>
</style>

<body>
</body>

</html>
'''

msg.attach(MIMEText(body,'html'))

filename = 'RCOEM_1.pdf'
attachment = open(filename, 'rb')

p = MIMEBase('application','octet-stream')

p.set_payload((attachment).read())

encoders.encode_base64(p)

p.add_header('Content-Disposition',"attachment; filename=%s" % filename)

msg.attach(p)

server = smtplib.SMTP('smtp.gmail.com',587)
server.starttls()
server.login(from_mail,password)

text = msg.as_string()

server.send_message(msg)

print("success")

server.quit()
