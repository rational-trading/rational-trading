Note: Commands should be ran from this current folder.

# Setting up Django & Python venv

1) Install pip

2) Create a virtual environment\
    `python3 -m venv rational-trading-django-env`

3) Activate the venv\
    Windows: `rational-trading-django-env\Scripts\activate.bat`\
    Unix: `source rational-trading-django-env/bin/activate`

4) Install Django\
    `python -m pip install -r requirements.txt`

5) Check that the installation was successful\
    `import django` should return no errors in a python terminal inside the venv

6) Deactivate the terminal when not working on Django\
    `deactivate`

# Workflow

1) Activate venv - check step 2 above

2) Update dependencies and libraries\
    `python -m pip install -r requirements.txt`

3) If installed a new library - i.e. matplotlib, update the requirements.txt file\
    `pip freeze > requirements.txt`\
    and make sure you commit the new requirements file!

4) You can run the webserver with\
    `python manage.py runserver`.\
    It should automatically restart whenever you make changes.

5) View the Swagger API docs by going to http://127.0.0.1:8000/api/docs#/. This page will allow you to view the available endpoints and make test requests in browser.

6) Typecheck your Python code with `python check.py`

7) Deactivate venv when finished working.

# Database

1) To initialise the database, use `python manage.py migrate`

2) To create a login for the admin interface (at `/admin`), use `python manage.py createsuperuser`

3) If you make a change to the model, create a migration using `python manage.py makemigrations models`

4) If there are any unapplied migrations, re-run `python manage.py migrate`

5) In the worst case, delete `db.sqlite3` (and possible `models/migrations`) and re-initialise.
