apt-get update && apt-get install -y openssh-server openssh-client 
mkdir -vp /var/run/sshd 
echo root:2wsx@WSX | chpasswd 
echo "Port 56001" >> /etc/ssh/sshd_config 
echo "PermitRootLogin yes" >> /etc/ssh/sshd_config 
echo "AllowTcpForwarding yes" >> /etc/ssh/sshd_config

mkdir -p /var/run/sshd && mkdir -vp /etc/ssh 
cat /etc/ssh/ssh_config | grep -v StrictHostKeyChecking > /etc/ssh/ssh_config.new 
echo "    StrictHostKeyChecking no" >> /etc/ssh/ssh_config.new 
mv /etc/ssh/ssh_config.new /etc/ssh/ssh_config

mkdir ~/.ssh && touch ~/.ssh/authorized_keys 
echo "ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABgQC78F+oSl5ebEIghIWCUM4W4+vZQum/+QjUGk2EUdDPorDbxRaaFUX8fdIhMvg/u7vFQlf6m8fIgNba3V0Ly3s6Nwny9wv52aSlK5Dm8XmWYamQFBIk6kSiA5CnyaGTU2Q7c0LTJ6sa3sK81t536gfV0WLmFGhKcF8qidbRcLPfoy4T/42J5MzQIUNAs7Wn0jHmJttUqDOS3F4wRhuQkyEJgY3Ssi/lFprB1FgSgR4c0a6Z3hLQE+EbE7NIBDjwJXe+3zCqPKqu+ykY9PHN1IkdlXqQbXkU4S4MKXUE0aYrEuavNjXUCBHNQiKEyRdLP0AUVW7FR7BzzPrhAunVSa59I+Law9xpYoJb3K5yCHPrWUmR6Gpvmcm/ceQV38rwFmKyI3sSNMh/28h20kVgeaBrCYrGhLS5Z1kcOu8sVFOSOlL1R3m4fvf8xata02J66w+q4LE06yYiHM+elocCG4m8ZRBxpwaFlALK8dw2P+jFT2V4nuX1C0lJMpObsQsbsS0= danerli@DANERLI-MB1" >> ~/.ssh/authorized_keys

/usr/sbin/sshd -D &

ps -ef  | grep sshd
