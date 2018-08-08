BRaID-Project

An interactive database allowing access and analysis of experimental data. The project uses the Django web framework in order to create a database and a series of webapages that can be used to modify and access the data.

REQUIREMENTS

The project requirements are in requirements.txt. This project assumes that Python 3 version has been installed. First git clone the project and then from the command line go inside the ‘braid-master’ folder.
Type pip install -r requirements.txt to install the necessary components.
Follow the instructions given here to install sqlite on your system. http://www.sqlitetutorial.net/download-install-sqlite/

.ENV file

The DEBUG should be set to True when making changes to code except in production when it should be set to FALSE
The secret key can be ignored for debugging/writing code purposes 
The DATABASE_URL points to the location where the sqlite will store the db file. ‘sqlite://’ is part of the protocol and should be there. One ‘/’ afterwards indicates relative pathing while ‘//’ indicates absolute. ‘..’ stand for go up the folder. Thus, the path in the .env from the GitHub will store the db file in the ‘braid’ directory as db.sqlite3. 


BRAID-MASTER/BRAID/BRAID FOLDER

In settings.py in INSTALLED_APPS ‘experiments’ has already been added. Experiments is the name of the app where the database experiments are being done. 

BRAID-MASTER/BRAID/EXPERIMENTS FOLDER

Models.py has the database setup. This file has all the tables and their relationships. This file has been written according to the Django framework. The official documentation for Django https://docs.djangoproject.com/en/2.0/intro/tutorial01/ is quite simple and straightforward to understand. 

BRAID-MASTER/BRAID/EXPERIMENTS/MANAGEMENT/COMMANDS

The init-data.py is where all the data is being put into the database. Right now, this file to a very good extent represents the data available in the NCGR servers. 

RUN PROGRAM
To run the program, go to BRAID-MASTER/BRAID folder and in the console type ‘python manage.py makemigrations’. This shall setup the Django to create the database tables according to the specifications provided in the models.py. To create the database structure type ‘python manage.py migrate’ afterwards. Then go to BRAID/BRAID folder and type ‘python manage.py init-data’ to populate the database. 
