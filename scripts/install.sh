#!/usr/bin/env bash

sed -i.bak -e '6,9d;' /home/vagrant/.bashrc
echo export DJANGO_DIR=/vagrant >> /home/vagrant/.bashrc
source /home/vagrant/.bashrc

echo "-----updates-----"
apt-get -y install ifupdown
apt-get -y update
apt-get -y upgrade
apt-get -y install python3-pip
apt-get -y install postgresql postgresql-contrib

# Installation des dépendances python
echo "-----Install depedances-----"
pip3 install --upgrade pip
python3 -m pip install -r $DJANGO_DIR/requirements.txt
echo "-----END-----"