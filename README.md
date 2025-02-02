# Multilingual FAQ System

A Django-based FAQ management system with multilingual support and WYSIWYG editor.

## Features

- Multilingual FAQ management (English, Hindi, Bengali)
- WYSIWYG editor for rich text formatting using CKEditor
- Automatic translation using Google Translate API
- REST API with language selection
- Django Admin interface for content management
- Caching for improved performance

## Prerequisites

- Python 3.8+
- Virtual Environment

## Installation

1. Create and activate virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

2. Install dependencies:
```bash
cd backend
pip install -r requirements.txt
```

3. Run migrations:
```bash
python manage.py migrate
```

4. Create superuser:
```bash
python manage.py createsuperuser
```
Default credentials:
- Username: admin
- Password: admin123

5. Start the server:
```bash
python manage.py runserver
```

## API Endpoints

1. List all FAQs (English):
```
GET http://localhost:8000/api/faqs/
```

2. List FAQs in Hindi:
```
GET http://localhost:8000/api/faqs/?lang=hi
```

3. List FAQs in Bengali:
```
GET http://localhost:8000/api/faqs/?lang=bn
```

4. Create new FAQ:
```
POST http://localhost:8000/api/faqs/
Content-Type: application/json

{
    "question": "What is this?",
    "answer": "This is a multilingual FAQ system."
}
```

## Usage

1. Access the admin interface at http://localhost:8000/admin/
2. Log in with your superuser credentials
3. Click on "FAQs" to add or edit FAQ entries
4. The WYSIWYG editor will be available for formatting answers
5. Translations will be generated automatically when you save

## Features in Detail

### Multilingual Support
- Questions and answers are automatically translated to Hindi and Bengali
- Fallback to English if translation is unavailable
- Language selection via API query parameter

### WYSIWYG Editor
- Rich text formatting for answers
- Support for images, links, and formatting
- Available in Django admin interface

### Caching
- Responses are cached for improved performance
- Cache is automatically invalidated when content is updated

## License

MIT License
