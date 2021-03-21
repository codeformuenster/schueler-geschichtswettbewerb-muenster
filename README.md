The website folder contains the prototype for the website.

The url localhost/karte presents the starting view of the prototype.

localhost/karte/karte contains the map with all locations marked on it. Clicken on a marker shows the name of the location and provides a link to a detailed view of the location

localhost/karte/orte displays a list of all locations that are entered in the database. The list can be filtered by name. Every entry links to a detail view that shows the location on a map and lists all submissions related to the location.

A django admin user exists with the following login data:
  user: admin
  password: Geschichtswettbewerb123

with python manage.py createsuperuser a new one can be added.
Under localhost/admin the database entries can be edited. This includes the possibility to add new ones and remove entries. 
The page to edit place entries (localhost/admin/karte/ort) includes the functionality to reverse-geocode the entered place to a location.

In the Website/geschichtswettbewerb/geschichtswettbewerb/settings.py file the connection to the sql database needs to be made. Once the connection is established, the database needs to be migrated to the project.

All python packages needed for the django project and all other scripts are listed in the requirements.txt file. Additional software, that is necessary is listed below:

python 3.8.2
mysql 8.0.22
gdal 3.2.1
geos 3.9.1
mysqlclient 2.0.1
postgresql 13.2
postgis 3.1.1

With the command python manage.py runserver, the website will be started on the localhost. The command has to be run in the Website/geschichtswettbewerb directory.

The dump files contain the underlying database with all their entries.

The query.py file contains the Query class with methods to execute all queries as defined in the 2020_11_11_Verschlage_Suchanfragen.pdf file.

The insertData.py file is a simple script that can be used to enter .xlsx tables into the database.

The tables file contains all database tables in an .xlsx format that was used to correct all entries.

The Geocoding Scripts file contains all scripts used to convert places to coordinates for OpenStreetMap maps.
