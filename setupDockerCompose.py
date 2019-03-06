# -*- coding:utf8 -*-
import os
# 安装docker
def setupDocker():
    os.system('sudo yum remove docker docker-client docker-client-latest docker-common docker-latest docker-latest-logrotate docker-logrotate docker-selinux docker-engine-selinux docker-engine')
    os.system('sudo yum install -y yum-utils device-mapper-persistent-data lvm2')
    os.system('sudo yum-config-manager --add-repo http://mirrors.aliyun.com/docker-ce/linux/centos/docker-ce.repo')
    os.system('sudo yum install -y docker-ce')
    os.system('sudo systemctl start docker')
setupDocker()
# 安装docker-compose
def setupCompose():
    os.system('sudo curl -L "https://github.com/docker/compose/releases/download/1.23.2/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose')
    os.system('sudo chmod +x /usr/local/bin/docker-compose')
    os.system('sudo ln -s /usr/local/bin/docker-compose /usr/bin/docker-compose')
setupCompose()