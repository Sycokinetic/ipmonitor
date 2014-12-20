Author: Alexander Gunter

== Description ==
This is a python script that will periodically check and store the machine's
external IP and will send out emails notifying of changes. This is primarily
targeted at home-based servers where the external IP periodically changes.

The script utilizes two plain text files, and there is an installation script.

ipmonitor.py is the core python script. It utilizes ipgetter to check the
machine's external IP and uses the sendemail utility to send email
notifications only when the IP changes.

email_list is a plain text file storing the list of emails to send
notifications to. Each email is on its own line.

recorded_ip is a plain text file storing the last known external IP.

install.sh is the bash installation script. It will prompt you for the
location to copy ipmonitor.py to, installing to /var/run/ by default.
email_list and recored_ip will be created in /etc/ipmonitor/. To enter
the list of emails, type them in and separate each with only a comma and no
spaces. If one does not exist, it will then create a cron job that will run
every ten minutes.

== Installation ==
To use the install script, have install.sh and ipmonitor.py in the same
directory. Make install.sh executable and run it with "./install.sh". You
will need to use your password for sudo, but do not run as "sudo ./install.sh"
because this breaks setting up the cron job.

== Default File Locations ==
/var/run/ipmonitor.py
/etc/ipmonitor/email_list
/etc/ipmonitor/recorded_ip

== Dependencies ==
Python 2.7 or probably Python 3
ipgetter module (install with pip)
sendemail command line tool
