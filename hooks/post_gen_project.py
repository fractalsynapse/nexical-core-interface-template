"""
NOTE:
    the below code maintains the Python Nexical Core
    CookieCutter Django project initialization

    * It managed the OS license and community files
    * It sets local environment variables
    * It generates the GitHub CI/CD workflow

TODO: add membership based ecommerce system
"""

from __future__ import print_function

import json
import os
import random
import shutil
import string

try:
    # Inspired by
    # https://github.com/django/django/blob/master/django/utils/crypto.py
    random = random.SystemRandom()
    using_sysrandom = True
except NotImplementedError:
    using_sysrandom = False

TERMINATOR = "\x1b[0m"
WARNING = "\x1b[1;33m [WARNING]: "
INFO = "\x1b[1;33m [INFO]: "
HINT = "\x1b[3;33m"
SUCCESS = "\x1b[1;32m [SUCCESS]: "


def generate_random_string(length, using_digits=False, using_ascii_letters=False, using_punctuation=False):
    """
    Example:
        opting out for 50 symbol-long, [a-z][A-Z][0-9] string
        would yield log_2((26+26+50)^50) ~= 334 bit strength.
    """
    if not using_sysrandom:
        return None

    symbols = []
    if using_digits:
        symbols += string.digits
    if using_ascii_letters:
        symbols += string.ascii_letters
    if using_punctuation:
        all_punctuation = set(string.punctuation)
        # These symbols can cause issues in environment variables
        unsuitable = {"'", '"', "\\", "$"}
        suitable = all_punctuation.difference(unsuitable)
        symbols += "".join(suitable)
    return "".join([random.choice(symbols) for _ in range(length)])


def generate_random_user():
    return generate_random_string(length=32, using_ascii_letters=True)


def set_flag(file_path, flag, value=None, formatted=None, *args, **kwargs):
    if value is None:
        random_string = generate_random_string(*args, **kwargs)
        if random_string is None:
            print(
                "We couldn't find a secure pseudo-random number generator on your "
                "system. Please, make sure to manually {} later.".format(flag)
            )
            random_string = flag
        if formatted is not None:
            random_string = formatted.format(random_string)
        value = random_string

    with open(file_path, "r+") as f:
        file_contents = f.read().replace(flag, value)
        f.seek(0)
        f.write(file_contents)
        f.truncate()

    return value


def replace_file(read_file_path, write_file_path):
    with open(read_file_path, "r+") as rf:
        file_contents = rf.read()

        with open(write_file_path, "r+") as wf:
            wf.seek(0)
            wf.write(file_contents)
            wf.truncate()


def set_django_secret_key(file_path):
    django_secret_key = set_flag(
        file_path,
        "!!!SET DJANGO_SECRET_KEY!!!",
        length=64,
        using_digits=True,
        using_ascii_letters=True,
    )
    return django_secret_key


def set_postgres_user(file_path, value):
    postgres_user = set_flag(file_path, "!!!SET POSTGRES_USER!!!", value=value)
    return postgres_user

def set_postgres_password(file_path):
    postgres_password = set_flag(
        file_path,
        "!!!SET POSTGRES_PASSWORD!!!",
        length=64,
        using_digits=True,
        using_ascii_letters=True,
    )
    return postgres_password


def set_redis_password(file_path):
    redis_password = set_flag(
        file_path,
        "!!!SET REDIS_PASSWORD!!!",
        length=64,
        using_digits=True,
        using_ascii_letters=True,
    )
    return redis_password


def set_public_env():
    django_env_path = os.path.join(".env", ".django")
    postgres_env_path = os.path.join(".env", ".postgres")
    redis_env_path = os.path.join(".env", ".redis")

    set_django_secret_key(django_env_path)

    set_postgres_user(postgres_env_path, value=generate_random_user())
    set_postgres_password(postgres_env_path)

    set_redis_password(redis_env_path)


def set_secret_env():
    secret_env_path = os.path.join(".env", ".secret")

    with open(secret_env_path, "w+") as f:
        f.writelines("""
# Mailgun
# ------------------------------------------------------------------------------
MAILGUN_API_KEY="{{ cookiecutter.mailgun_api_key }}"
MAILGUN_WEBHOOK_KEY="{{ cookiecutter.mailgun_webhook_key }}"
MAILGUN_DOMAIN="{{ cookiecutter.mailgun_domain }}"

# Email
# ------------------------------------------------------------------------------
DJANGO_DEFAULT_FROM_EMAIL="{{ cookiecutter.from_email }}"
CONTACT_NOTIFICATION_EMAIL="{{ cookiecutter.contact_email }}"
""")


def remove_open_source_files():
    file_names = ["CONTRIBUTORS.txt", "LICENSE"]
    for file_name in file_names:
        os.remove(file_name)


def set_cicd():
    cookiecutter_cicd_path = os.path.join(".github", "cookiecutter")
    app_cicd_path = os.path.join(cookiecutter_cicd_path, "cicd.yml")

    workflow_cicd_path = os.path.join(".github", "workflows")
    active_cicd_path = os.path.join(workflow_cicd_path, "cicd.yml")

    replace_file(app_cicd_path, active_cicd_path)

    shutil.rmtree(cookiecutter_cicd_path, ignore_errors=True)


def main():
    set_public_env()
    set_secret_env()

    if "{{ cookiecutter.open_source_license }}" == "Not open source":
        remove_open_source_files()

    set_cicd()

    print(SUCCESS + "Project initialized." + TERMINATOR)


if __name__ == "__main__":
    main()