# Animated Octo Eureka

[![Built with Cookiecutter Django](https://img.shields.io/badge/built%20with-Cookiecutter%20Django-ff69b4.svg?logo=cookiecutter)](https://github.com/cookiecutter/cookiecutter-django/)
[![Black code style](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/ambv/black)

Powered by [Cookiecutter Django](https://github.com/cookiecutter/cookiecutter-django), Animated Octo Eureka is a boilerplate for jumpstarting
production-ready Django projects quickly.

-   Documentation: <https://cookiecutter-django.readthedocs.io/en/latest/>
-   See [Troubleshooting](https://cookiecutter-django.readthedocs.io/en/latest/troubleshooting.html) for common errors and obstacles

## Features

-   For Django 4.0
-   Works with Python 3.10
-   Renders Django projects with 100% starting test coverage
-   Twitter [Bootstrap](https://github.com/twbs/bootstrap) v5
-   [12-Factor](http://12factor.net/) based settings via [django-environ](https://github.com/joke2k/django-environ)
-   Secure by default. We believe in SSL.
-   Optimized development and production settings
-   Registration via [django-allauth](https://github.com/pennersr/django-allauth)
-   Comes with custom user model with [JWT authentication](https://www.django-rest-framework.org/api-guide/authentication/#json-web-token-authentication) ready to go
-   Basic ASGI setup for Websockets
-   Media storage using Amazon S3, Google Cloud Storage or Azure Storage
-   Docker support using [docker-compose](https://github.com/docker/compose) for development and production (using [Traefik](https://traefik.io/) with [LetsEncrypt](https://letsencrypt.org/) support)
-   Run tests with unittest or pytest
-   Runs PostgreSQL 14.1
-   Default integration with [pre-commit](https://github.com/pre-commit/pre-commit) for identifying simple issues before submission to code review
-   Configuration for [Celery](https://docs.celeryq.dev) and [Flower](https://github.com/mher/flower) (the latter in Docker setup only)
-   Integration with [MailHog](https://github.com/mailhog/MailHog) for local email testing
-   Integration with [Sentry](https://sentry.io/welcome/) for error logging

## Usage
For local development, see the following:

-   [Developing locally](http://cookiecutter-django.readthedocs.io/en/latest/developing-locally.html)
-   [Developing locally using docker](http://cookiecutter-django.readthedocs.io/en/latest/developing-locally-docker.html)
