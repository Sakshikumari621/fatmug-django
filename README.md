# fatmug-django : Processing Video

This project provides a web application that allows users to upload videos, process them in the background to extract subtitles, and display these subtitles as closed captions. The application supports multiple language subtitles and includes search functionality within the video. 

## Prerequisites

- Python 3.12+
- Django
- PostgreSQL
- Docker
- ffmpeg
- Dependencies listed in `requirements.txt`

## Configuration Guide for Database Credentials

This section provides instructions on how to configure the PostgreSQL database credentials. The credentials are stored in a `.env` file located in the project directory.

The file should be structured as follows:

```bash
DATABASE_NAME=db_name             
DATABASE_USER=db_user_name         
DATABASE_PASSWORD=your_db_password  
DATABASE_HOST=db_host
DATABASE_PORT=db_post

```

## Installation

1. **Clone the Repository:**
```bash
git clone https://github.com/Sakshikumari621/fatmug-django.git
cd fatmug-django
```

2. **Setup Docker:**
```bash
docker-compose build
```
```bash
docker-compose up -d
```
3. **Create a Superuser:**
```bash
docker-compose exec django-app python manage.py createsuperuser
```

Access the Django admin interface at `http://127.0.0.1:8000/admin/` using the superuser credentials created earlier.

Upload the vidoes at `http://127.0.0.1:8000/upload/`