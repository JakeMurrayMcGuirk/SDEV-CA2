# SDEV-CA2
Hi youd need the following pip installments to run this project 

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
pip intsall django ruff
pip install django uritemplate



Ive created a file.db file in the project directory so run this command 

If you are using a Unix/Linix/Mac

export DATABASE_URL=sqlite:///file.db   


If you are using Windows 

set DATABASE_URL=sqlite:///file.db



Then please make sure to unset db after you finish working or set it in a venv :


for mac /linix
unset DATABASE_URL


for windows:
Remove-Item env:\DATABASE_URL
