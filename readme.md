## Creating virtual environment
1) make venv:
   * python -m venv venv
2) active venv:
   * source venv/bin/activate
3) install requirement:
   * pip install -r req.txt


## prepare database:
1) install postgresql:
   * sudo apt install postgresql postgresql-contrib
2) install postgis for gis map:
   *sudo apt install postgis postgresql-12.4-postgis (use your postgresql version)
3) connect to postgresql and make db and user:
   * sudo psql -U postgres
   * create database [dbname];
   * create user [user] with encrypted password '[pass]';
   * grant all privileges on database [dbname] to [user];
   * \c [dbname]
   * create extension postgis;
   * create extension postgis_topology;
   * \q

## config django:
1) set database and user info in settings.py in DATABASES part
2) migrate:
   * python manage.py makemigrations
   * python manage.py migrate
3) create superuser:
   * python manage.py createsuperuser

## run project:
1) add driver path to project:
   * export PATH=$PATH:[path to]/gis/reporter
2) run project:
   * python manage.py runserver
   * go to: http://127.0.0.1:8000/admin/
