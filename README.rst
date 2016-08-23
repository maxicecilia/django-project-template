{% if False %}
Installation
------------

To start a new project with this template::

    django-admin.py startproject \
      --template=https://github.com/caktus/django-project-template/zipball/master \
      --extension=py,rst,yml \
      --name=Makefile,gulpfile.js,package.json
      <project_name>

{% endif %}
{{ project_name|title }}
========================

Below you will find basic setup and deployment instructions for the {{ project_name }}
project. To begin you should have the following applications installed on your
local development system:

- Python >= 2.7
- `pip <http://www.pip-installer.org/>`_ >= 1.5
- `virtualenv <http://www.virtualenv.org/>`_ >= 1.10
- `virtualenvwrapper <http://pypi.python.org/pypi/virtualenvwrapper>`_ >= 3.0
- git >= 1.7

Django version
------------------------

The Django version si configured in ``requirements/base.txt``, you should update it to the newest LTS version if possible.

Postgres
------------------------
By default the makefile script will use a {{project_name}} user to create the proper database, create it if it doesn't exists
    $ sudo su postgres
    $ psql
    > CREATE USER {{project_name}} WITH SUPERUSER PASSWORD '{{project_name}}';

Getting Started
------------------------

First clone the repository from Github and switch to the new directory::

    $ git clone git@github.com:natgeo/{{ project_name }}.git
    $ cd {{ project_name }}

To setup your local environment you can use the quickstart make target `setup`, which will
install both Python and Javascript dependencies (via pip and npm) into a virtualenv named
"{{ project_name }}", configure a local django settings file, and create a database via
Postgres named "{{ project_name }}" with all migrations run::

    $ make setup
    $ workon {{ project_name }}

If you require a non-standard setup, you can walk through the Makefile to understand the required steps.

If necessary, create the Postgres database and run the initial migrate::

    ({{ project_name }})$ createdb -E UTF-8 {{ project_name }}
    ({{ project_name }})$ python manage.py migrate
