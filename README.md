# Check Nanterre 

## Prérequis
* Virtualbox, outil de virtualisation - [Télécharger Virtualbox](https://www.virtualbox.org/wiki/Downloads)
* Vagrant, gestionnaire de machine virtuelle - [Télécharger vagrant](https://www.vagrantup.com/downloads.html)

# Lancer le serveur

* Cloner ce dépôt
* une fois cloner, placez vous dans le répertoire du projet
* Faites un `vagrant up`
* Une fois l'installation terminée, faites un `vagrant ssh` pour accéder à la VM
* Allez dans le répertoire des fichiers de sources avec la commande `cd /vagrant`
* Entrez les commandes suivantes :
  - `python3 manage.py makemigrations` et `python3 manage.py migrate` pour créer le schéma de la base de données

* Puis faites la commande suivante pour lancer le serveur `python3 manage.py runserver 0.0.0.0:8000`
