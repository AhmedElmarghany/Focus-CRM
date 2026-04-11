# Focus CRM

A modern, responsive landing page for CRM system, built with Django and Bootstrap. Designed with a strong **UI/UX and frontend design**.

The application provides an interface for managing **CRUD operations** for managing customer records, organized **search functionality**, and secure **access control**.

---

[Live Demo](https://ahmedelmarghany.pythonanywhere.com/)

---

## Key Features

**Core Functionality**

- User-Friendly Interface
- 100% Responsive Design
- Custom 404 Error Page

- User Authentication (Login & Signup)
- CRUD Operations (Create, Read, Update, Delete Records)
- Search Functionality
- Access Control (Protected Routes)

---

## Technologies

### Frontend
- **HTML**
- **CSS**
- **Bootstrap**
- **JavaScript (Vanilla)**
- **EmailJS** # For Sending Messages From contact form


### Backend
- **Django**
- **Python**
- **SQLite**

---

## Project Structure

```
Focus-CRM/
│
├── project/
│   ├── settings.py
│   ├── urls.py                # Main URL routing
│   ├── wsgi.py & asgi.py      # Server configurations
│   └── static/                # Project-level static files
│       ├── css/               # Custom stylesheets
│       │   ├── main.css       # Bootstrap styles
│       │   ├── navbar.css
│       │   ├── dashboard.css
│       │   ├── form.css
│       │   └── ...
│       ├── js/                # JavaScript files
│       │   ├── form.js
│       │   ├── alert.js       # Alert notifications
│       │   ├── scrollTracker.js
│       │   └── bootstrap.bundle.min.js
│       ├── fonts/             # Custom local fonts "IBM Plex Sans" & "IBM Plex Serif"  
│       └── images/            # Images & Logos
│
├── webapp/                     # Django application (main CRM logic)
│   ├── models.py              # Database models (Record -Customer-, Category)
│   ├── views.py               # View handlers & logic
│   ├── forms.py               # Django forms
│   ├── urls.py                # App URL routing
│   ├── admin.py
│   └── migrations/            # Database migrations
│
├── templates/                 # HTML templates
│   ├── base.html              # Base template
│   ├── pages/
│   │   ├── index.html
│   │   ├── login.html
│   │   ├── update-record.html
│   │   ├── search.html
│   │   ├── 404.html
│   │   └── ...
│   └── components/            # Reusable components
│       ├── navbar.html
│       ├── footer.html
│       ├── alert.html
│       ├── logout-modal.html
│       └── ...
│
├── staticfiles/               # Collected static files (for production)
├── db.sqlite3                 # SQLite database
├── manage.py
└── requirements.txt

```

### Important Static Files

**Bootstrap & CSS Framework:**
- [project/static/css/main.css](project/static/css/main.css) - Main stylesheet
- [project/static/js/bootstrap.bundle.min.js](project/static/js/bootstrap.bundle.min.js) - Bootstrap JavaScript bundle (responsive components)

**Fonts & Icons:**
- [project/static/fonts/](project/static/fonts/) - Custom web fonts
- [project/static/icons/](project/static/icons/) - SVG/icon assets

---

## Dependencies & Requirements

### Python Packages

```
asgiref==3.11.1
crispy-bootstrap5==2026.3
Django==6.0.3
django-crispy-forms==2.6
sqlparse==0.5.5
tzdata==2025.3
```

---

## Prerequisites

Before running the project, ensure you have:

1. **Python 3.10+** installed on your system
2. **pip** (Python package manager)
3. **Git** (optional, for version control)

---

## How to Run

### 1. Clone/Setup the Project

```bash
# Navigate to project directory
cd Focus-CRM
```

### 2. Create and Activate Virtual Environment

**On Windows (PowerShell):**
```bash
python -m venv venv
.\venv\Scripts\Activate
```

**On macOS/Linux:**
```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Apply Database Migrations

```bash
python manage.py migrate
```

### 5. Create Superuser (Admin Account) (optional)

```bash
python manage.py createsuperuser
# Follow the prompts to create an admin user
```

### 6. Run Development Server

```bash
python manage.py runserver
```

The application will be available at: `http://127.0.0.1:8000/`

### 7. Access the Application

- **Main Page:** http://127.0.0.1:8000/
- **Admin Panel:** http://127.0.0.1:8000/admin/
- **Login:** http://127.0.0.1:8000/login/
- **Contact Us:** http://127.0.0.1:8000/contact-us/
- **Dashboard:** http://127.0.0.1:8000/dashboard/

---

## Screenshots

<img width="1914" height="1111" alt="1" src="https://github.com/user-attachments/assets/af8df590-a49d-455d-8a58-b450ba326a1b" />

---

<img width="1914" height="1044" alt="2" src="https://github.com/user-attachments/assets/f2edd111-fe2d-44a4-9653-b88c83c727f9" />

---

<img width="1919" height="869" alt="3" src="https://github.com/user-attachments/assets/e2c2f362-e0a8-4283-a12a-29c4503f40e2" />

---

<img width="1914" height="867" alt="4" src="https://github.com/user-attachments/assets/68a3899a-3a8f-4313-a187-9098eb569155" />

---

<img width="1919" height="869" alt="5" src="https://github.com/user-attachments/assets/768b3cbc-3e78-4150-aaef-c0325904ee1b" />

---

<img width="1919" height="869" alt="6" src="https://github.com/user-attachments/assets/3f197bd6-d404-44a6-b02a-37ab3949c82d" />

---

<img width="1290" height="922" alt="7" src="https://github.com/user-attachments/assets/39e5cbeb-6ff5-4384-b7e9-2e9565d1a624" />

---

<img width="1919" height="869" alt="8" src="https://github.com/user-attachments/assets/dd275688-3490-430e-8cc8-6ef6bef02e30" />

