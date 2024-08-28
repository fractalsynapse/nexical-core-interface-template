#!/bin/sh
# this is a very simple script that tests the docker configuration for cookiecutter-django
# it is meant to be run from the root directory of the repository, eg:
# sh tests/test_docker.sh

set -o errexit
set -x

# create a cache directory
mkdir -p .cache/docker
cd .cache/docker

# create the project using the default settings in cookiecutter.json
cookiecutter ../../ --no-input --overwrite-if-exists "$@"
cd nexical_core_interface

# make sure all images build
docker compose build

# run the project's tests
docker compose run ui pytest --ds=config.settings.local.ui -o 'python_files=test_ui_*.py'
docker compose run api pytest --ds=config.settings.local.api -o 'python_files=test_api_*.py'

# return non-zero status code if there are migrations that have not been created
docker compose run api python manage.py makemigrations --dry-run --check || { echo "ERROR: there were changes in the models, but migration listed above have not been created and are not saved in version control"; exit 1; }

# Test support for translations
docker compose run api python manage.py makemessages --all

# Make sure the check doesn't raise any warnings
docker compose run \
  -e DJANGO_SECRET_KEY="$(openssl rand -base64 64)" \
  -e DJANGO_ADMIN_PATH=x \
  -e MAILGUN_API_KEY=x \
  -e MAILGUN_DOMAIN=x \
  -e DJANGO_SECURE_SSL_REDIRECT=True \
  ui python manage.py check --settings=config.settings.production.ui --deploy --database default --fail-level WARNING

# Run npm build script if package.json is present
if [ -f "package.json" ]
then
    docker compose run node npm run build
fi
