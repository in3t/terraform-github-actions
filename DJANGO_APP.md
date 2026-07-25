# Sample Django Web Application

A simple Django web application with a contact form built with Python and Django.

## Features

- **Responsive UI** with modern gradient design
- **Contact Form** with name, email, and message fields
- **Form Validation** - server-side and client-side validation
- **AJAX Form Submission** - smooth form handling without page reloads
- **Success/Error Messages** - user feedback after form submission
- **CSRF Protection** - Django built-in security

## Project Structure

```
.
├── manage.py                 # Django management command
├── myproject/               # Main project settings
│   ├── settings.py          # Django configuration
│   ├── urls.py              # URL routing
│   ├── asgi.py              # ASGI configuration
│   └── wsgi.py              # WSGI configuration
├── home/                    # Django app
│   ├── views.py             # View functions
│   ├── urls.py              # App URL patterns
│   ├── models.py            # Database models
│   ├── admin.py             # Admin configuration
│   ├── apps.py              # App configuration
│   ├── tests.py             # Unit tests
│   ├── migrations/          # Database migrations
│   └── templates/home/      # HTML templates
│       └── index.html       # Homepage
├── db.sqlite3               # SQLite database
└── venv/                    # Python virtual environment
```

## Installation & Setup

### Prerequisites
- Python 3.8+
- pip (Python package manager)

### Step 1: Create Virtual Environment
```bash
python -m venv venv
```

### Step 2: Activate Virtual Environment
**Windows:**
```bash
.\venv\Scripts\activate
```

**macOS/Linux:**
```bash
source venv/bin/activate
```

### Step 3: Install Dependencies
```bash
pip install django
```

### Step 4: Run Migrations
```bash
python manage.py migrate
```

### Step 5: Start Development Server
```bash
python manage.py runserver
```

The application will be available at `http://localhost:8000`

## Usage

1. Open your browser and navigate to `http://localhost:8000/`
2. Fill in the contact form with:
   - Your name
   - Your email address
   - Your message
3. Click "Send Message"
4. The form will be submitted via AJAX, and you'll see a success/error message

## API Endpoints

### GET / 
Returns the homepage with the contact form

**Response:** HTML page with contact form

### POST /submit/
Handles form submission

**Request Parameters:**
- `name` (string, required) - User's name
- `email` (string, required) - User's email
- `message` (string, required) - User's message

**Response (JSON):**
```json
{
  "status": "success",
  "message": "Hello [name]! Your message has been received.",
  "data": {
    "name": "[name]",
    "email": "[email]"
  }
}
```

**Error Response:**
```json
{
  "status": "error",
  "message": "All fields are required"
}
```

## File Descriptions

### home/views.py
Contains view functions:
- `home()` - Renders the homepage
- `submit_form()` - Handles form submission via POST request

### home/urls.py
URL routing for the home app:
- `/` - Maps to home view
- `/submit/` - Maps to submit_form view

### home/templates/home/index.html
Frontend HTML template with:
- Responsive design with CSS styling
- Contact form with three input fields
- JavaScript for AJAX form submission
- Success/error message display

### myproject/settings.py
Django configuration including:
- Installed apps list (includes 'home')
- Middleware configuration
- Database settings (SQLite)
- Static files configuration

### myproject/urls.py
Main URL router that includes the home app URLs

## Deployment

For production deployment, follow Django's deployment checklist:

1. Set `DEBUG = False` in settings.py
2. Configure `ALLOWED_HOSTS` with your domain
3. Use a production database (PostgreSQL recommended)
4. Use a production web server (Gunicorn, uWSGI)
5. Set up HTTPS/SSL
6. Configure static files serving
7. Use environment variables for secrets

Example production run with Gunicorn:
```bash
pip install gunicorn
gunicorn myproject.wsgi:application --bind 0.0.0.0:8000
```

## Testing

Run the test suite:
```bash
python manage.py test
```

## Creating a Superuser (Admin)

```bash
python manage.py createsuperuser
```

Then access the admin at `http://localhost:8000/admin`

## Customization

### Modify the Form
Edit `home/templates/home/index.html` to add/remove form fields

### Change Styling
Update the `<style>` section in `home/templates/home/index.html`

### Add Database Models
Create models in `home/models.py` and run migrations:
```bash
python manage.py makemigrations
python manage.py migrate
```

## Troubleshooting

**Port Already in Use:**
```bash
python manage.py runserver 8001  # Use different port
```

**Database Issues:**
```bash
python manage.py migrate --run-syncdb
```

**Static Files Not Loading:**
```bash
python manage.py collectstatic --noinput
```

## Dependencies

- Django 6.0.7+
- Python 3.8+

## License

This is a sample application for learning purposes.

## Resources

- [Django Documentation](https://docs.djangoproject.com/)
- [Django Deployment Guide](https://docs.djangoproject.com/en/stable/howto/deployment/)
- [Django Security Guide](https://docs.djangoproject.com/en/stable/topics/security/)
