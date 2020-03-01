import smtplib

smtp_user = 'XXXXXXXX'
smtp_password = 'XXXXXXXX'
smtp_server = "XXXXXXXX"
smtp_port = XXX

to = [input("Enter the email address you'd like to send to :")]
subject = input("Enter the subject :")
body = input("Enter the body :")

email_text = """\
From: %s
To: %s
Subject: %s

%s
""" % (sent_from, ", ".join(to), subject, body)

try:
    server = smtplib.SMTP_SSL(smtp_server, smtp_port)
    server.ehlo()
    server.login(smtp_user, smtp_password)
    server.sendmail(smtp_user, to, email_text)
    server.close()

    print("Email sent!")
except:
    print('Email not sent!')
