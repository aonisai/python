# -*- coding: utf-8 -*-

import smtplib
from email.mime.text import MIMEText
from email.header import Header
from email.utils import formatdate

gmail_address = 'seiunryou0602@gmail.com'
gmail_passwd = 'eqqtgihmqaqfwgrf'
#'09020893402oku!'

gmail_smtp_address = 'smtp.gmail.com'
gmail_smtp_port = 587

from_address = 'seiunryou0602@gmail.com'
to_address = 'yanoakio0601@gmail.com'

charset = 'ISO_2022_jp'
subject = u'title'
text = u'test_mail'

msg = MIMEText(text.encode(charset), 'plain', charset)
msg['Subject'] = Header(subject, charset)
msg['From'] = from_address
msg['To'] = to_address
msg['Date'] = formatdate(localtime=True)

smtpobj = smtplib.SMTP(gmail_smtp_address, gmail_smtp_port)
smtpobj.ehlo()
smtpobj.starttls()
smtpobj.ehlo()
smtpobj.login(gmail_address, gmail_passwd)
smtpobj.sendmail(from_address, to_address, msg.as_string())
smtpobj.close()

# smtp = smtplib.SMTP('gmail.com')
# smtp.sendmail(from_address, to_address, msg.as_string())
# smtp.close()