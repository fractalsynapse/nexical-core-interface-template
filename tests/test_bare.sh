#!/bin/sh
# this is a very simple script that tests the docker configuration for cookiecutter-django
# it is meant to be run from the root directory of the repository, eg:
# sh tests/test_bare.sh

set -o errexit
set -x

# Install OS deps
sudo scripts/install_os_dependencies.sh install

# create a cache directory
mkdir -p .cache/bare
cd .cache/bare

# create the project using the default settings in cookiecutter.json
cookiecutter ../../ --no-input --overwrite-if-exists "$@"
cd nexical_core_interface

# Install Python deps
pip install -r requirements/local.txt

# run the project's tests
pytest --ds=config.settings.local.ui -o 'python_files=test_ui_*.py'
pytest --ds=config.settings.local.api -o 'python_files=test_api_*.py'

# Make sure the check doesn't raise any warnings
python manage.py check --fail-level WARNING

# Run npm build script if package.json is present
if [ -f "package.json" ]
then
    npm install
    npm run build
fi
