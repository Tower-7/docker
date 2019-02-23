# -*- coding:utf8 -*-
import os
# 安装docker
os.system('sudo yum remove docker docker-client docker-client-latest docker-common docker-latest docker-latest-logrotate docker-logrotate docker-selinux docker-engine-selinux docker-engine')
os.system('sudo yum install -y yum-utils device-mapper-persistent-data lvm2')
os.system('sudo yum-config-manager --add-repo http://mirrors.aliyun.com/docker-ce/linux/centos/docker-ce.repo')
os.system('sudo yum install -y docker-ce')
os.system('sudo systemctl start docker')
