# 云开发机设置

## ubuntu系统使用 root 用户登录实例

```shell
# step1 
# 按照文档执行https://cloud.tencent.com/document/product/1207/44569#ubuntu-.E7.B3.BB.E7.BB.9F.E5.A6.82.E4.BD.95.E4.BD.BF.E7.94.A8-root-.E7.94.A8.E6.88.B7.E7.99.BB.E5.BD.95.E5.AE.9E.E4.BE.8B.EF.BC.9F

sudo passwd root
sudo vim /etc/ssh/sshd_config
## PermitRootLogin 参数修改为 yes
## PasswordAuthentication 参数修改为 yes

# step2
ssh-copy-id root@lrhome.vip

```
