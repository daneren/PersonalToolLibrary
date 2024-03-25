#!/bin/bash


# aria2
# https://zhuanlan.zhihu.com/p/637294044?utm_id=0
# centos 7
# https://github.com/git-lfs/git-lfs/blob/main/INSTALLING.md


# Read the ID and VERSION_ID from /etc/os-release
. /etc/os-release

# Check the ID and VERSION_ID and perform the appropriate operation
if [ "$ID" = "ubuntu" ]; then
    # install aria2
    sudo apt update && sudo apt install aria2
    # install git-lfs
    curl -s https://packagecloud.io/install/repositories/github/git-lfs/script.deb.sh | sudo bash
    apt-get install git-lfs

elif [ "$ID" = "centos" ]; then
    # install aria2
    sudo yum update && sudo yum install epel-release aria2
    # install git-lfs
    curl -s https://packagecloud.io/install/repositories/github/git-lfs/script.rpm.sh | sudo os=el dist=$VERSION_ID bash
    yum install git-lfs -y
else
    echo "This is not Ubuntu or CentOS 7/8."
fi


# download df-data download tool
# https://gist.github.com/padeoe/697678ab8e528b85a2a7bddafea1fa4f
wget https://hf-mirror.com/hfd/hfd.sh
chmod a+x hfd.sh