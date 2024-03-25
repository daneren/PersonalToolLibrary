# 1、环境准备

```bash
# aria2
# https://zhuanlan.zhihu.com/p/637294044?utm_id=0
# centos
sudo yum update && sudo yum install epel-release aria2
# ubuntu
sudo apt update && sudo apt install aria2

# centos 7
# https://github.com/git-lfs/git-lfs/blob/main/INSTALLING.md
curl -s https://packagecloud.io/install/repositories/github/git-lfs/script.rpm.sh | sudo os=el dist=7 bash
yum install git-lfs -y

# download df-data download tool
# https://gist.github.com/padeoe/697678ab8e528b85a2a7bddafea1fa4f
wget https://hf-mirror.com/hfd/hfd.sh
chmod a+x hfd.sh
```

# 2、使用

## 下载数据集

```shell
HF_ENDPOINT=https://hf-mirror.com bash /mnt/cfs/danerli/datasets/tools/hfd.sh Skywork/SkyPile-150B --dataset --local-dir /mnt/cfs/danerli/datasets/tools/SkyPile-150B --tool aria2c -x 4
```

## 下载模型

```shell
HF_ENDPOINT=https://hf-mirror.com bash /mnt/cfs/danerli/datasets/tools/hfd.sh Qwen/Qwen1.5-14B-Chat --local-dir /mnt/cfs/tilearn/pretrain_models/Qwen1.5-14B-Chat --tool aria2c -x 4
```

