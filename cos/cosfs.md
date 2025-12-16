# 安装脚本

```bash
git clone https://github.com/tencentyun/cosfs /usr/cosfs

sudo yum update && sudo yum install automake gcc-c++ git libcurl-devel libxml2-devel fuse-devel make openssl-devel fuse

cd /usr/cosfs
./autogen.sh
./configure
make
sudo make install
cosfs --version  #查看 cosfs 版本号

echo user:id:key > /etc/passwd-cosfs

chmod 640 /etc/passwd-cosfs

mkdir -vp /mnt/cfs/danerli/datasets/data_datasets

cosfs user /root/danerli/datasets/data_datasets -ourl=https://cos.ap-shanghai.myqcloud.com -odbglevel=info -onoxattr -oallow_other

umount -l /mnt/cfs/danerli/datasets/data_datasets
```



# reference

[1]: https://cloud.tencent.com/developer/article/1855290	"CentOS 7 挂载腾讯云COS对象存储教程"

