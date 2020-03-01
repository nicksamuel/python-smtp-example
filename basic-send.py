import smtplib


gmail_user = 'apikey'
gmail_password = 'INSERT PASSWORD HERE'

sent_from = gmail_user
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
    server = smtplib.SMTP_SSL('smtp.sendgrid.com', 465)
    server.ehlo()
    server.login(gmail_user, gmail_password)
    server.sendmail(sent_from, to, email_text)
    server.close()

    print("Email sent!")
except:
    print('Something went wrong...')
