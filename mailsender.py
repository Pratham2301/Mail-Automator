import smtplib as s
from credentials import *

ob = s.SMTP("smtp.gmail.com", 587)
ob.starttls()

ob.login(my_email, my_password)

subject = my_subject

body = my_body

message = "Subject:{}\n\n{}".format(subject, body)

mail_from = my_email
mail_to = my_to_list

ob.sendmail(mail_from, mail_to, message)

print("send succesfully")

ob.quit()
