import ipgetter
import os
import smtplib
from email.mime.text import MIMEText

def sendEmail(ip):
	#emailFilename = "/etc/ipmonitor/email_list"
	senderEmail = "ipmonitor-noreply@gmail.com"
	emailFilename = "email_list"
	if not os.path.isfile(emailFilename):
		print("Error - {0} not found".format(emailFilename))
	else:
		with open(emailFilename, "r") as emailFile:
			for email in emailFile:
				email = email.strip()
				SENDMAIL = "/usr/sbin/sendmail" # sendmail location
				p = os.popen("%s -t" % SENDMAIL, "w")

				p.write("To: {0}\n".format(email))
				p.write("Subject: Home IP Changed: {0}\n".format(ip))
				p.write("\n") # blank line separating headers from body
				p.write("Home IP has changed to {0}\n".format(ip))
				sts = p.close()
				if sts != 0:
				    print("Sendmail exit status", sts)

def main():
	curIP = ipgetter.myip()

	#recIPfilename = "/etc/ipmonitor/current_ip"
	recIPfilename = "current_ip"

	if not os.path.isfile(recIPfilename):
		recIPfile = open(recIPfilename, "w")
		recIPfile.write(curIP)
		recIPfile.close()
	else:
		recIPfile = open(recIPfilename, "r")
		#recIP = recIPfile.readline().strip()
		recIP = ""
		recIPfile.close()
		if recIP != curIP:
			recIPfile = open(recIPfilename, "w")
			recIPfile.write(curIP)
			sendEmail(curIP)

if __name__ == "__main__":
	main()
