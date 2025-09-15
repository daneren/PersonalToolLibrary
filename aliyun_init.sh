

apt-get update
apt-get install docker.io

fdisk -l
mkfs -t ext4 /dev/vdb
mkdir -vp /mnt/data
mount /dev/vdb /mnt/data


# 修改docker数据存储路径
sudo sh -c 'mkdir -p /etc/docker && echo '\''{"data-root": "/mnt/data/dockerfiles"}'\'' > /etc/docker/daemon.json'

sudo systemctl restart docker
