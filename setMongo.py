# -*- coding:utf8 -*-
import os
# set mongo
os.system('docker pull mongo')
os.system('mkdir -p /usr/local/mongo')
os.system('cd /usr/local/mongo && docker run -p 15015:27017 -v $PWD/db:/data/db -d mongo')

