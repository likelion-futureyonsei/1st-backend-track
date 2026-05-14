python3 -m venv .venv
MAC: source .venv/bin/activate
pip install djangorestframework
django-admin startproject mangeLikelion
python ./manage.py migrate
python ./manage.py runserver
django-admin startapp babylion
