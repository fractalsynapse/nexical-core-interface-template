"""
NOTE:
    the below code maintains the Python Nexical Core
    CookieCutter Django project initialization

    * It sets local environment variables
    * It managed the OS license and community files
    * It generates the GitHub CI/CD workflow

TODO: add membership based ecommerce system
"""

from __future__ import print_function

TERMINATOR = "\x1b[0m"
WARNING = "\x1b[1;33m [WARNING]: "
INFO = "\x1b[1;33m [INFO]: "
HINT = "\x1b[3;33m"
SUCCESS = "\x1b[1;32m [SUCCESS]: "

# The content of this string is evaluated by Jinja, and plays an important role.
# It updates the cookiecutter context to trim leading and trailing spaces
# from domain/email values
"""
{{ cookiecutter.update({ "domain_name": cookiecutter.domain_name | trim }) }}
{{ cookiecutter.update({ "from_email": cookiecutter.from_email | trim }) }}
{{ cookiecutter.update({ "contact_email": cookiecutter.contact_email | trim }) }}
{{ cookiecutter.update({ "mailgun_api_key": cookiecutter.mailgun_api_key | trim }) }}
{{ cookiecutter.update({ "mailgun_webhook_key": cookiecutter.mailgun_webhook_key | trim }) }}
{{ cookiecutter.update({ "mailgun_domain": cookiecutter.mailgun_domain | trim }) }}
"""

project_slug = "{{ cookiecutter.project_slug }}"
if hasattr(project_slug, "isidentifier"):
    assert project_slug.isidentifier(), "'{}' project slug is not a valid Python identifier.".format(project_slug)

assert project_slug == project_slug.lower(), "'{}' project slug should be all lowercase".format(project_slug)
