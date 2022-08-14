from django.dispatch import Signal, receiver
import smtplib
notification=Signal(providing_args=['request','user'])
# HOST='smtp.mydomai.com'
# SUBJECT='Test emial from python'
# TO='mike@muslimapp.com'
# FROM='zar@zar.com'
# text='Loruim'
# BODY='\r\n'.join((
#     f'form: {FROM} ',
#     f'To: {TO} ',
#     f'Subject: {SUBJECT} ',
#     '',
#     text,
# ))
# server=smtplib.SMTP(HOST)
# server.sendmail(FROM,[TO],BODY)
# server.quit()
@receiver(notification)
def show_notification(sender,**kwargs):
    pass