#!/usr/bin/env python2

import sys
import requests as req
import smtplib
from string import Template
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from st2common.runners.base_action import Action

class MyEchoAction(Action):   	
    def run(self, url):	
	flag=1
	try:
		resp = req.get(url,timeout=6.0)
		print(resp.status_code)
		print(resp.url)	
		print('Email sent')
	except req.exceptions.MissingSchema:
                print("invalid URL")
		flag=0
                sys.exit(0)		
	except req.exceptions.Timeout:
                print("Request timeout")
		flag=0
                sys.exit(0)

        if flag==1:
		MY_ADDRESS = 'stackstorm.alert@gmail.com'
		TO='bhagyashridesh09@gmail.com'
		PASSWORD = 'ganpatibappa'
		s = smtplib.SMTP(host='smtp.gmail.com', port=587)
		s.starttls()
		s.login(MY_ADDRESS, PASSWORD)
		msg = MIMEMultipart()       
		message = 'action executed successfully'		
		msg['From']=MY_ADDRESS
		msg['To']='bhagyashridesh09@gmail.com'
		msg['Subject']="This is TEST"
		msg.attach(MIMEText(message, 'plain'))
		s.sendmail(MY_ADDRESS, [TO], msg.as_string())
		del msg
                s.quit()
