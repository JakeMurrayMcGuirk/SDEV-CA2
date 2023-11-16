# SDEV-CA2

Hi , Youd need to  initialise a pip env envornment in the project directory to run our project , I've added all the necessary packages to it run :

pipenv shell


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