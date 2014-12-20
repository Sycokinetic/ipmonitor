managerFile="ipmonitor.py"

printf "Enter installation location for ipmonitor.py (default: /usr/bin/): "
read managerTarget

if [ -z $managerTarget ]
then
	managerTarget="/usr/bin/"
fi
sudo cp $managerFile $managerTarget

printf "Enter comma-separated list of emails to notify: "
read emailList

arr=$(echo $emailList | tr "," "\n")

sudo mkdir /etc/ipmonitor
sudo touch /etc/ipmonitor/recorded_ip

for email in $arr
do
	#sudo echo $email >> /etc/ipmonitor/email_list
	echo $email | sudo tee -a /etc/ipmonitor/email_list
done

managerPath=$managerTarget$managerFile
if [ -z "$(crontab -l | grep $managerFile)" ]
then
	crontab -l | { cat; echo "*/10 * * * * $managerPath"; } | crontab -
fi
