# -*- coding:utf8 -*-
import os
# 安装git
os.system('yum -y install git')
os.system('mkdir /config')
# 安装docker
def setupDocker():
    os.system('cd /config && git clone https://github.com/Tower-7/docker.git')
    os.system('cd /config/docker && python setupDocker.py')
# 安装kubernetes
setupDocker()
def setupKubernetes():
    os.system('cd /config && git clone https://github.com/Tower-7/kubernetes.git')
    os.system('cd /config/kubernetes && python setupKubernetes.py')
setupKubernetes()