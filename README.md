# 安装前准备
yum install -y git &&\
mkdir -p /config && \
cd /config && \
git clone https://github.com/Tower-7/docker.git && \
cd docker && \
python setupDockerCompose.py

#测试是否安装成功
docker ps
docker-compose -v
