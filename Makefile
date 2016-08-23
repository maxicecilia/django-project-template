PROJECT_NAME = {{ project_name }}

default: lint test

test:
	# Run all tests and report coverage
	# Requires coverage
	python manage.py makemigrations --dry-run | grep 'No changes detected' || \
		(echo 'There are changes which require migrations.' && exit 1)
	coverage run manage.py test
	coverage report -m --fail-under 80

lint-py:
	# Check for Python formatting issues
	# Requires flake8
	flake8 .

lint: lint-py

# Generate a random string of desired length
generate-secret: length = 32
generate-secret:
	@strings /dev/urandom | grep -o '[[:alnum:]]' | head -n $(length) | tr -d '\n'; echo

setup:
	virtualenv -p `which python2.7` $(WORKON_HOME)/{{ project_name }}
	$(WORKON_HOME)/{{ project_name }}/bin/pip install -U pip wheel
	$(WORKON_HOME)/{{ project_name }}/bin/pip install -Ur requirements/development.txt
	$(WORKON_HOME)/{{ project_name }}/bin/pip freeze
	cp {{ project_name }}/settings/local.example.py {{ project_name }}/settings/local.py
	echo "DJANGO_SETTINGS_MODULE={{ project_name }}.settings" > .env
	cd {{project_name}}/settings/environment_overrides && ln -s development.py active.py && cd ../../../
	createdb {{ project_name }} -U {{ project_name }} -W -h 127.0.0.1
	$(WORKON_HOME)/{{ project_name }}/bin/python manage.py migrate
	git hooks install
	@echo
	@echo "The {{ project_name }} project is now setup on your machine."
	@echo "Run the following commands to activate the virtual environment and run the"
	@echo "development server:"
	@echo
	@echo "	workon {{ project_name }}"

update:
	$(WORKON_HOME)/{{ project_name }}/bin/pip install -U -r requirements/dev.txt
