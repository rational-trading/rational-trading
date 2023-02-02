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

1) Running the webserver\
    `python manage.py runserver`

2) Deactivate venv when finished working.
