import smtplib



sender = "pydhpe@gmail.com"
password = "Scorpion12"
recipient = "prnv.ds@gmail.com"
subject = "test email from pyton "
text = "hello from python\nThis is line 2\n this is line 3"
smtp_server = smtplib.SMTP_SSL("smtp.gmail.com",465)
smtp_server.login(sender,password)
message = "subject: {}\n\n{}".format(subject,text)
smtp_server.sendmail(sender,recipient, message,)
smtp_server.close()


