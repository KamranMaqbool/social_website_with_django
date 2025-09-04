python -m pip install Django

django-admin startproject bookmarks     (create a new project)

django-admin startapp AppName           (create new app)

python -m pip install django-extensions

python -m pip install social-auth-app-django

python -m pip install werkzeug 

(You will need to install Werkzeug, which contains a debugger layer required by the RunServerPlus
extension of Django Extensions. Use the following command to install Werkzeug:)

python manage.py runserver_plus --cert-file cert.crt
(Run webiste for https)

python manage.py runserver_plus --cert-file cert.crt --key-file cert.key 0.0.0.0:8000

