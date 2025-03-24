# CropCareServer

This is a backend web application built with Django, designed to serve as the backend for the CropCare Mobile application.
``
  git clone https://github.com/pryogendra/Digital_Farming_Plateform.git
``
The project uses Django REST framework to provide API endpoints and can be easily extended for additional functionality.

## Table of Contents

1. [Installation](#installation)
2. [Setup](#setup)
3. [Usage](#usage)
4. [Configuration](#configuration)
5. [Testing](#testing)
6. [Deployment](#deployment)
7. [License](#license)

## Installation

### Prerequisites
- Python 3.x
- pip (Python package installer)

### Install the dependencies

Clone the repository:

```bash
git clone https://github.com/pryogendra/CropCareServer.git
cd CropCareServer
```

Create and activate a virtual environment:

```bash
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```

Install the necessary dependencies:

```bash
pip install -r requirements.txt
```

## Setup

### Configure Database

By default, the project uses SQLite as the database, but you can configure it to use other databases like PostgreSQL or MySQL by modifying the `DATABASES` setting in `settings.py`.

To set up the database:

```bash
python manage.py migrate
```

This will apply the necessary database migrations.

### Create a Superuser

To access the Django admin panel and manage your application data:

```bash
python manage.py createsuperuser
```

Follow the prompts to set up the superuser account.

### Static Files

Collect static files (CSS, JavaScript, images):

```bash
python manage.py collectstatic
```

## Usage

### Running the Development Server

To start the development server, run:

```bash
python manage.py runserver
```

This will run the server on `http://127.0.0.1:8000/`. You can navigate to this URL in your browser.

### API Endpoints

If you're using Django REST Framework for API endpoints, they will be available at the following URLs (customize as per your application):

- `/api/v1/endpoint/` - Description of endpoint.
- `/api/v1/another-endpoint/` - Description of another endpoint.

Refer to the documentation for more detailed information about available endpoints.

### Accessing the Admin Panel

To access the Django admin panel, navigate to:

```
http://127.0.0.1:8000/server_admin/
```

Log in using the superuser credentials you created earlier.

**Screenshots**

![Screenshot From 2025-03-24 13-41-03](https://github.com/user-attachments/assets/a105df1f-9717-4fbe-9b3f-2a3c4b569cf5)
![Screenshot From 2025-03-24 13-41-14](https://github.com/user-attachments/assets/ea45c87d-27e0-4759-ac49-01076ebcb7ab)


## Configuration

The settings for the application can be modified in the `settings.py` file. Some of the key configurations include:

- **DEBUG**: Set to `False` for production environments.
- **ALLOWED_HOSTS**: List of allowed host/domain names.
- **DATABASES**: Database settings (SQLite by default, but can be changed to PostgreSQL/MySQL).
- **CORS**: If your frontend is hosted separately, enable Cross-Origin Resource Sharing (CORS) with the `django-cors-headers` package.

## Deployment

For deploying the application to a production environment, follow these steps:

1. Set `DEBUG = False` in `settings.py`.
2. Set up a production database (e.g., PostgreSQL).
3. Configure a web server such as Nginx to serve the application.
4. Use a WSGI server like Gunicorn to run the app.
5. Set up environment variables for sensitive information such as API keys and database credentials.
