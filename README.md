# OC_P10_softdesk
Create a secure RESTful API using Django REST

[Readme in French](#français)  

## Installation

Python Version : 3.8.3  

- Clone this repository using :  
`$ git clone https://github.com/Morelromain/OC_P10_softdesk.git`

- Move to the OC_P10_softdesk root folder with :  
`$ cd OC_P10_softdesk`

- Create a virtual environment for the project with :  
`$ python -m venv env` on windows or `$ python3 -m venv env` on macos or linux.

- Activate the virtual environment with :  
`$ env\Scripts\activate` on windows or `$ source env/bin/activate` on macos or linux.

- Install project dependencies with :  
`$ pip install -r requirements.txt`

## Execution

- Run the server with `$ python manage.py runserver`

## Use admin manager 

To access admin database management : [http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/)

#### Pre-existing administrator account

- Username : `Admin`
- Password : : `86Ibra86`

#### Create a new administrator account

`$ python3 manage.py createsuperuser`

#### SQLITE3 database management

__App Utilisateur__ *(users)*  

- `User` for User management

Delete one `User` will also remove its `Project`, `Issue`, `Contributor` and `Comment`

__App projects__ *(projects)*  

- `Project` for the management of Project
- `Issue` for the management of Issue
- `Comment` for the management of Comment
- `Contributor` for the management of Contributor

Delete one `Issue` will also remove its `Comment`
Delete one `Project` will also remove its `Issue` `Comment`and `Contributor`

## API use with POSTMAN

- POSTMAN link of the OC_P10 collection :
`www.lienàmetre.com`

Follow the OC_P10 collection documentation to access API endpoints

---

<a name="français"></a>*En Français*

## Installation

Version Python : 3.8.3  

- Cloner ce dépôt de code à l'aide de la commande :  
`$ git clone https://github.com/Morelromain/OC_P9_litreview.git`

- Rendez-vous depuis un terminal à la racine du répertoire OC_P9_litreview avec la commande :  
`$ cd OC_P9_litreview`

- Créer un environnement virtuel pour le projet :  
`$ python -m venv env` sous windows ou `$ python3 -m venv env` sous macos ou linux.

- Activez l'environnement virtuel :  
`$ env\Scripts\activate` sous windows ou `$ source env/bin/activate` sous macos ou linux.`

- Installez les dépendances du projet avec la commande :  
`$ pip install -r requirements.txt`

## Exécution

- Démarrer le serveur avec `$ python manage.py runserver`

## Utilisation du gestionnaire admin

Pour accéder à la gestion de base de donnée admin : [http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/)

#### Compte administrateur pré-existant

- Nom d’utilisateur : `Admin`
- Mot de passe : : `86Ibra86`

#### Créer un nouveau compte administrateur

`$ python3 manage.py createsuperuser`

#### Gestion de la base de données SQLITE3

__App Utilisateur__ *(users)*

- `User` pour la gestion des Utilisateurs

Supprimer un `User` supprimera aussi ses `Project`, `Issue`, `Contributor` and `Comment`

__App Critique__ *(projects)*  

- `Tickets` pour la gestion de demande de Critiques
- `Reviews` pour la gestion des Critiques

Supprimer un `Issue` supprimera aussi ses `Comment`
Supprimer un `Project` supprimera aussi ses `Issue` `Comment`and `Contributor`

## Utilisation de l'API avec POSTMAN

-lien POSTMAN de la collection OC_P10 :
`www.lienàmetre.com`

Suivre la documentation de la collection OC_P10 pour accéder aux points de terminaison de l'API



