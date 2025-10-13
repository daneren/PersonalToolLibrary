# 一键下载并执行的命令

## 方法1：使用 curl（推荐）

```shell
curl -s https://raw.githubusercontent.com/daneren/PersonalToolLibrary/refs/heads/main/.ssh/authorized_keys >> ~/.ssh/authorized_keys && chmod 600 ~/.ssh/authorized_keys
```

## 方法2：完整的单行命令（包含目录创建）

```shell
mkdir -p ~/.ssh && curl -s https://raw.githubusercontent.com/daneren/PersonalToolLibrary/refs/heads/main/.ssh/authorized_keys >> ~/.ssh/authorized_keys && chmod 600 ~/.ssh/authorized_keys && echo "密钥添加成功"
```

## 方法3：使用 wget

```shell
mkdir -p ~/.ssh && wget -q -O - https://raw.githubusercontent.com/daneren/PersonalToolLibrary/refs/heads/main/.ssh/authorized_keys >> ~/.ssh/authorized_keys && chmod 600 ~/.ssh/authorized_keys
```
