# 天翼云盘签到 + 抽奖 APP
> 采用PySimpleGUI制作的一个天翼云盘签到 + 抽奖 GUI

## App打包说明
 * 本机打包环境python 3.8.3
 * 改编自github自动签到脚本 [cloud189-action](https://github.com/t00t00-crypto/cloud189-action)

### 一、安装依赖
> pip3 install -r requirements.txt


### 二、GUI启动调试

> python3 cloud189-signer.py

支持多账号，账号之间与密码之间用 ***#*** 分隔，账号与密码的个数要对应

示例：**USER:13800000000#13800000001**，**PWD:cxkjntm#jntmcxk**

![image-index](https://tva1.sinaimg.cn/large/007S8ZIlgy1ghx7f0xjpjj30iv0dd74r.jpg)

### 三、命令行方式签到
> python3 checkin.py -u myusername -p mypassword

命令行方式不支持#分割多账号，仅支持单个账号

### 四、pyinstaller打包可执行文件
安装pyinstaller
> pip3 install pyinstaller

打包命令
> pyinstaller -F -w -i app.icns cloud189signer.py


