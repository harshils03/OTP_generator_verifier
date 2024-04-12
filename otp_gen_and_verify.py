import random
import sys

def create_otp():
	g_otp = random.randint(1000,9999)
	sg_otp = str(g_otp)
	return sg_otp
otp = create_otp()


def main():
	print("-----------------------------")
	name = input("Enter your name: ")
	email = input("Enter your email address: ")
	print("-----------------------------")
	return name,email


name,reciever_mail = main()


import pymysql as pm
def check_email_exists(email):
    conn = pm.connect(host='localhost', user='root', database='otp_gen', password='root')
    cur = conn.cursor()
    query = "SELECT * FROM custom_details WHERE email = %s"
    cur.execute(query, (email,))
    result = cur.fetchone()
    conn.close()
    if result:
        return True
    else:
        return False

check_mail = check_email_exists(reciever_mail)
if check_mail:
	print("You are already verified")
	sys.exit()
else:
	print("Lets get you verified")



import smtplib
from email.mime.text import MIMEText

def send_email(subject, body, sender, recipients, password):
	msg = MIMEText(body)
	msg['Subject'] = subject
	msg['From'] = sender
	msg['To'] = ', '.join(recipients)
	with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp_server:
		smtp_server.login(sender, password)
		smtp_server.sendmail(sender, recipients, msg.as_string())
	print("OTP sent, Check your MAIL!!")
	


sender_email = "harshil.s1403@gmail.com"
body = "Your otp is "+otp
# receiver_email = "simratenterprises7@gmail.com"
subject = "You have recieved an OTP"
smtp_server = "smtp.gmail.com"
smtp_port = 465#for SSL
smtp_username = "harshil.s1403@gmail.com"
password = "tizi bopt xiwr grjw"


send_email(subject, body, sender_email, reciever_mail, password)


def verify():	
	while True:
		print("-----------------------------")
		enterotp = int(input("Enter your otp: "))
		if enterotp == int(otp):
			print("Correct!! You are verified")
			print("-----------------------------")
			break
		else:
			print("Not correct, Enter again!!")
		continue
		print("-----------------------------")
verify()


conn = pm.connect(host = 'localhost',user = 'root',database= 'otp_gen',password= 'root')
cur = conn.cursor()
query = "insert into custom_details (name,email) values (%s,%s)"
cur.execute(query, (name,reciever_mail))
conn.commit()















