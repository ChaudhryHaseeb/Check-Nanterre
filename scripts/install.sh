#!/usr/bin/env bash

sed -i.bak -e '6,9d;' /home/vagrant/.bashrc
echo export DJANGO_DIR=/vagrant >> /home/vagrant/.bashrc
echo export DATABASE_NAME=checknanterre >> /home/vagrant/.bashrc
echo export DATABASE_USER=checknanterreuser >> /home/vagrant/.bashrc
echo export DATABASE_HOST='localhost' >> /home/vagrant/.bashrc
echo export DATABASE_PORT='' >> /home/vagrant/.bashrc
echo export DATABASE_PASSWORD=checknanterre >> /home/vagrant/.bashrc
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

# Création de l'utilisateur pour la BDD
sudo su - postgres -c psql <<EOF
CREATE DATABASE $DATABASE_NAME;
CREATE USER $DATABASE_USER WITH PASSWORD '$DATABASE_PASSWORD';

ALTER ROLE $DATABASE_USER SET client_encoding TO 'utf8';
ALTER ROLE $DATABASE_USER SET default_transaction_isolation TO 'read committed';
ALTER ROLE $DATABASE_USER SET timezone TO 'UTC';

GRANT ALL PRIVILEGES ON DATABASE $DATABASE_NAME TO $DATABASE_USER;
ALTER USER $DATABASE_USER CREATEDB;
EOF