#!/usr/bin/env bash

export DJANGO_DIR=/vagrant >> /home/vagrant/.bashrc
source /home/vagrant/.bashrc

echo "-----updates-----"
apt-get -y install ifupdown
sudo apt-get update
apt-get -y upgrade
apt-get -y install python3-pip

# Installation des dépendances python
echo "-----Install depedances-----"
pip3 install --upgrade pip
python3 -m pip install -r $DJANGO_DIR/requirements.txt
echo "-----END-----"