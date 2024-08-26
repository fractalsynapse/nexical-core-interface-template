# Cookiecutter Nexical Core Interface

[![Build Status](https://img.shields.io/github/actions/workflow/status/fractalsynapse/nexical-core-interface-template/cicd.yml?branch=main)](https://github.com/fractalsynapse/nexical-core-interface-template/actions/workflows/cicd.yml?query=branch%3Amain)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/ambv/black)

[![Join our Discord](https://img.shields.io/discord/1259252913138700380
?style=flat&logo=discord&logoColor=white)](https://discord.gg/7kJCN6EtQA)

Powered by [Cookiecutter](https://github.com/cookiecutter/cookiecutter), Nexical Cookiecutter Core Interface Template is a framework for jumpstarting
production-ready Django Nexical frontend sites quickly.

- If you have problems with Cookiecutter Django, please open [issues](https://github.com/fractalsynapse/nexical-core-interface-template/issues/new) don't send
  emails to the maintainers.

## Usage

Let's pretend you want to create a Nexical project called "redditresearch". Rather than using `startproject` and then editing the results to include your name, email, and various configuration issues that always get forgotten until the worst possible moment, get [cookiecutter](https://github.com/cookiecutter/cookiecutter) to do all the work.

First, get Cookiecutter:

    $ pip install "cookiecutter>=1.7.0"

Now run it against this repo:

    $ cookiecutter https://github.com/fractalsynapse/nexical-core-interface-template

You'll be prompted for some values. Provide them, then a Nexical Core Interface Django project will be created for you.

Answer the prompts with your own desired options. For example:

    Cloning into 'nexical-core-interface-template'...
    remote: Counting objects: 550, done.
    remote: Compressing objects: 100% (310/310), done.
    remote: Total 550 (delta 283), reused 479 (delta 222)
    Receiving objects: 100% (550/550), 127.66 KiB | 58 KiB/s, done.
    Resolving deltas: 100% (283/283), done.
    project_name [Nexical Core Interface]: Reddit Research
    project_slug [reddit_research]: reddit
    description [Starter project for building Django based Nexical AI interfaces]: A reddit research platform.
    Select open_source_license:
    1 - Apache Software License 2.0
    2 - Not open source
    Choose from 1, 2 [1]: 1
    domain_name [nexical.ai] reddit.example.com
    from_email [Nexical AI <noreply@nexical.ai>]: adrian@fractalsynapse.com
    contact_email [hello@nexical.ai]: adrian@fractalsynapse.com
    mailgun_api_key []: ...,
    mailgun_webhook_key []: ...,
    mailgun_domain []: reddit.example.com

Enter the project and take a look around:

    $ cd reddit/
    $ ls

Create a git repo and push it there:

    $ git init
    $ git add .
    $ git commit -m "Initial commit."
    $ git remote add origin git@github.com:fractalsynapse/reddit_research.git
    $ git push -u origin main

Now take a look at your repo.

## Community

- If you think you found a bug or want to request a feature, please open an [issue](https://github.com/fractalsynapse/nexical-core-interface-template/issues).
- For anything else, you can chat with us on [Discord](https://discord.gg/7kJCN6EtQA).

<img src="https://opencollective.com/cookiecutter-django/contributors.svg?width=890&button=false" alt="Contributors">

## Releases

Need a stable release? You can find them at <https://github.com/fractalsynapse/nexical-core-interface-template/releases>

## Not Exactly What You Want?

This is a starting point. _It might not be what you want._ If so, you have options:

### Fork This Template

If you have differences in your preferred setup, we encourage you to fork this to create your own version.
Once you have your fork working, let us know and I'll add it to a '_Similar Cookiecutter Templates_' list here.
It's up to you whether to rename your fork.

If you do rename your fork, I encourage you to submit it to the following places:

- [cookiecutter](https://github.com/cookiecutter/cookiecutter) so it gets listed in the README as a template.
- The cookiecutter [grid](https://www.djangopackages.com/grids/g/cookiecutters/) on Django Packages.

### Submit a Pull Request

We accept pull requests if they're small, atomic, and make the project development experience better.

## Articles

- [Why cookiecutter-django is Essential for Your Next Django Project](https://medium.com/@millsks/why-cookiecutter-django-is-essential-for-your-next-django-project-7d3c00cdce51) - Aug. 4, 2024
- [How to Make Your Own Django Cookiecutter Template!](https://medium.com/@FatemeFouladkar/how-to-make-your-own-django-cookiecutter-template-a753d4cbb8c2) - Aug. 10, 2023
- [Exploring with Cookiecutter](http://www.snowboardingcoder.com/django/2016/12/03/exploring-with-cookiecutter/) - Dec. 3, 2016
- [Introduction to Cookiecutter-Django](http://krzysztofzuraw.com/blog/2016/django-cookiecutter.html) - Feb. 19, 2016
