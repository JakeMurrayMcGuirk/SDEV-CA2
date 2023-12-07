# SDEV-CA2

1.  # Create a virtual env in the shoe-store directory and activate it ; 

python manage.py venv env 


2. # Install the required dependencies

you can just copy and paste them into your git bash or terminal system in the django SDEV-CA2,

pip install django-cors-headers

pip install dj-database-url

pip install python-dotenv

pip install djangorestframework

pip install factory-boy

pip install django-allauth

pip install dj-rest-auth

pip install django black

pip install django-storages

pip install django google-cloud-storage

pip install django gunicorn

pip install isort

pip install django Pillow

pip install django ruff

pip install django uritemplate


3. # Set the database

Ive created a file.db file in the shoe-store directory, its important to set this everytime before you run the project as it will contain all data required for the site to render all the information, if you dont set the db it wouldnt render the templates  so run this command 

If you are using a Unix/Linix/Mac

export DATABASE_URL=sqlite:///file.db   


If you are using Windows 

set DATABASE_URL=sqlite:///file.db


4.  # Run migrate 

Then after setting the db, run the migrate command :

python manage.py migrate 



## Then please make sure to unset db after you finish working or set it in a venv :

for mac /linix
unset DATABASE_URL


for windows:
Remove-Item env:\DATABASE_URL
