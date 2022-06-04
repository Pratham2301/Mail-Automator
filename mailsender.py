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
    <title>RCOEM WEBINAR</title>
</head>
<style>
    h1 {
        font-family: 'Gill Sans', 'Gill Sans MT', Calibri, 'Trebuchet MS', sans-serif;
        color: #f7f8f9;
    }

    .box {
        background-color: #384a5b;
        width: 100%;
        color: white;
        padding: 5%;
        border-radius: 20px;
    }

    body {

        margin-top: 5%;
        padding-left: 15%;
        padding-right: 15%;
        color: var(--primary-color);
        background-color: #212325;
        background: linear-gradient(45deg, #394754, #212325);
        font-family: 'Gill Sans', 'Gill Sans MT', Calibri, 'Trebuchet MS', sans-serif;
    }
</style>

<body>
    <div class="box">
        <h1 align="center">REMINDER</h1>
    Hello Enthusiast,
        <p class="content"> We are glad that you registered for the seminar on <strong>Blockchain</strong> brought to you by The
        <strong>Codebreakers x Lumos Labs.</strong>
        </p>
        <p class="list">
            Here are some important instructions about the seminar.<br><br>
            1. You are requested to carry your laptop as the session will be hands-on.<br>
            2. Due to heavy rush, the seating arrangements will be on a first come first serve basis.<br>
            3. We recommend you to go through the prerequisites and agenda (attached below) of the seminar for better outcomes.<br><br>

            <strong> Date: 04/06/22 </strong><br>
            <strong> Time: 1.00 p.m </strong><br><br>
            Please note the change in the venue.<br><br>
            The seminar will be conducted in the <strong>MBA Auditorium,RCOEM</strong> .<br><br>
        </p>
        <p >
            Regards,<br>
            Inshal Khan<br>
            President (The Codebreakers Club,RCOEM)<br>
        </p>


    </div>

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
