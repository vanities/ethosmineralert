#!/usr/bin/python3

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
	
			rigs = json['rigs']
			#print(rigs)

			my_rig = '44a642'

			rig = rigs[my_rig]
			print(rig)

			if rig['condition'] == 'unreachable':
				fromaddr = "ethosmineralert@hushmail.com"
				toaddr = "mischkeaa@gmail.com"

				# from
				message = "From: Me <" + fromaddr + ">\n"

				# to
				message += "To: Me <" + toaddr + ">\n"	
				 
				# subject
				message += "Subject: Miner is doing great!\n"

				# num of gpus
				message += rig['gpus'] + " gpu/s @ "

				message += rig['miner_hashes'] + " hashes per second."

				print(message)

				try:

					smtpserver = smtplib.SMTP('smtp.hushmail.com',587)
					smtpserver.ehlo()
					smtpserver.starttls()
					smtpserver.login(fromaddr, 'ethosmineralert')

					print('here')
					smtpserver.sendmail(fromaddr, toaddr, message)         
					print ("Successfully sent email")

					smtpserver.close()
				except:
				   print ("Error: unable to send email")


	# if time out
	except (HTTPError):
		print('Error: could not access ethos API!')

	
if __name__ == "__main__":
	main()