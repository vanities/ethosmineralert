#!/usr/bin/python3

''' ==========================
		Adam Mischke:
			ethOs mining alerter.

			Will email you the status of your rig, set on a schedule.
				Details:
					rig #, # of gpus, # hashrate
			If the miner goes down, it will send you an error.
	==========================
'''

''' json parsing '''
from json import loads
from urllib.request import urlopen, urlretrieve

''' smtp emailing '''
import smtplib


def main():
	# string containing the json api from ethos
	json_url = 'http://3d6870.ethosdistro.com/?json=yes'

	# make sure we recieve the object from the api
	try:
		with urlopen(json_url) as url:

			# read from the url
			json = loads(url.read().decode())
			#print(json)

	# if time out
	except:
		print('Error: could not access ethos API!')

	rigs = json['rigs']
	#print(rigs)

	my_rig = '44a642'

	rig = rigs[my_rig]
	print(rig)

	fromaddr = 'ethosmineralert@hushmail.com'
	password = 'ethosmineralert'
	toaddr = 'mischkeaa@gmail.com'
	host = 'smtp.hushmail.com'
	port = 587

	# from
	message = "From: Me <" + fromaddr + ">\n"

	# to
	message += "To: Me <" + toaddr + ">\n"	

	if rig['condition'] != 'unreachable':
		# subject
		message += "Subject: Miner is doing great!"

		# num of gpus
		message += rig['gpus'] + " gpu/s @ "

		# how many hashes they doing
		message += rig['miner_hashes'] + " hashes per second."
	else:
		# subject
		message += "Subject: Miner has lost connection!\n"
		# body
		message += "Please go check it out?"

		# make sure it looks good
		print(message)

	# try to send the connect to server email
	try:
		# connect to their server
		smtpserver = smtplib.SMTP(host,port)
	except:
		print ("Error: could not connect to host/port", host, port)

	smtpserver.ehlo()
	smtpserver.starttls()
	print("Server Connected")

	# try to authenticate
	try:
		# login user/password
		smtpserver.login(fromaddr, password)
		print("User/password authenticated")
	except SMTPAuthenticationError:
		print ("Error: could not authenticate user/password")

	# send it!
	smtpserver.sendmail(fromaddr, toaddr, message)         
	print ("Successfully sent email")

	# close the server
	smtpserver.close()
	
if __name__ == "__main__":
	main()