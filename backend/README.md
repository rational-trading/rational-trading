Note: Commands should be ran from the root folder of the project.

# Setting up Django & Python venv

1) Install pip

2) Create a virtual environment\
    `python3 -m venv backend/rational-trading-django-env`

2) Activate the venv\
    Windows: `backend\rational-trading-django-env\Scripts\activate.bat`\
    Unix: `source backend/rational-trading-django-env/bin/activate`

3) Install Django\
    `python -m pip install -r backend/requirements.txt`

4) Check that the installation was successful\
    `import django` should return no errors in a python terminal inside the venv

5) Deactivate the terminal when not working on Django\
    `deactivate`

# Workflow
1) Activate venv - check step 2 above

2) Update dependencies and libraries\
    `python -m pip install -r backend/requirements.txt`

3) If installed a new library - i.e. matplotlib, update the requirements.txt file\
    `pip freeze > backend/requirements.txt`\
and make sure you commit the new requirements file!

4) Running the webserver\
    `python backend/manage.py runserver`

5) Deactivate venv when finished working.
