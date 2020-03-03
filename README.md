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

# Préparer la configuration initiale

* Faites un `python3 manage.py createsuperuser` pour créer l'administrateur
* allez sur `localhost:8000/admin` et connectez-vous avec ces identifiants
* Créez un secrétaire :
  - dans Authentification>Utilisateur pour le créer
  - Utilisateurs pour l'associer au rôle secrétaire
* allez sur `localhost:8000/` et connectez-vous avec les identifiants créés précédemment et vous pourrez créer enseignants, promotions, étudiants et matières
  
# Dépôt mobile associé

* Accéder au dépôt associé - [dépôt mobile](https://github.com/anthonynascimento/heimdall_mobile)
