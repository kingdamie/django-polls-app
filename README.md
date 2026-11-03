# django-polls-app

A polling web app built with Django while following the official tutorial.
Visitors browse questions and their choices; admins manage polls through the Django admin.

## Features

- Public poll list and question detail pages
- Future-dated questions are hidden until their publish date
- Admin with inline choice editing, collapsible date section and a "Published recently?" column
- Automated tests for the model and views
- Static files (CSS and background image)

## Run it locally

```bash
pip install -r requirements.txt
python3 manage.py migrate
python3 manage.py createsuperuser
python3 manage.py runserver
```

- Polls: http://localhost:8000/polls/
- Admin: http://localhost:8000/admin/

## Run the tests

```bash
python3 manage.py test polls
```

## Configuration

Optional environment variables:

- `DJANGO_SECRET_KEY` - secret key (a development-only default is used if unset)
- `DJANGO_DEBUG` - set to `False` in production

## Status

Following the tutorial: voting and results pages are still to do.
