# MyPersonalizedProject

A Django-based web application designed with a clean project structure, environment-based settings, static/media separation, and deployment readiness.

This project was developed with a focus on maintainability, local development workflow, testing, and production deployment best practices.

---

## Features

- Django project with a custom project/app structure
- Environment-based configuration using `.env`
- Separated development and production settings logic
- Static files management with `collectstatic`
- Media files support for user uploads
- Responsive templates with static assets
- Root URL configured for the homepage
- Automated Django tests for core views
- Production-oriented deployment preparation

---

## Tech Stack

- Python
- Django
- python-dotenv
- SQLite (local development)
- PostgreSQL (production)
- Gunicorn
- Nginx
- HTML
- CSS
- JavaScript

---

## Project Structure
```text
MyPersonalizedProject/
├── PersonalProject/        # Django project configuration
├── myapp/                  # Main application
├── static/                 # Source static assets
├── templates/              # Shared templates
├── media/                  # Uploaded media files (not tracked in Git)
├── manage.py
├── requirements.txt
├── .env.example
└── README.md
