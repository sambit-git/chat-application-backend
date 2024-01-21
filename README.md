# Varta

Varta: A versatile chat application for users to engage in one-on-one and group conversations. Currently in development, with Django and Django Rest Framework powering the backend, and React handling the frontend. Stay tuned for upcoming features, as audio and video call functionality will be added in future updates.

## Setup

- git clone https://github.com/sambit-git/chat-application-backend.git
- cd chat-application-backend
- python -m venv venv
- source venv/bin/activate
- pip install -r ./requirements.txt
- cd varta
- mkdir static
- python manage.py makemigrations
- python manage.py migrate
- python manage.py createsuperuser (provide details as requested)
- python manage.py runserver
