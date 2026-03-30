# Focus CRM

Customer Relationship Management (CRM) system built with Django and Bootstrap.

## [Visit Live Demo](https://ahmedelmarghany.pythonanywhere.com/)
## 📋 Prerequisites

Before you begin, ensure you have the following installed:
- Python 3.8 or higher
- Node.js and npm (for frontend dependencies - not neccessary)
- pip (Python package installer)
- git

## 🚀 Installation & Setup

### 1. Clone the Repository
```bash
git clone https://github.com/AhmedElmarghany/Focus-CRM.git
cd Focus-CRM
```

### 2. Create Virtual Environment
```bash
# On Windows
python -m venv venv
venv\Scripts\activate

# On macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Backend Dependencies
```bash
pip install -r requirements.txt
```

### 5. Configure Django

The project uses Django's default SQLite database. To initialize the database:

```bash
python manage.py migrate
```

### 7. Run Development Server
```bash
python manage.py runserver
```

The application will be available at `http://localhost:8000`

## 📁 Project Structure

```
Focus-CRM/
├── project/   
│   ├── ...
│   └── static/                # Static files (CSS, JavaScript, images)
├── webapp/
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   ├── admin.py
│   └── migrations/
├── templates/                 # HTML templates
│   ├── base.html              # Base template
│   ├── landing/
│   │   └── index.html         # Landing page
│   └── components/            # Reusable template components
│       ├── navbar.html
│       ├── hero.html
│       ├── features.html
│       ├── pricing.html
│       ├── faq.html
│       ├── companies.html
│       └── footer.html
├── static/
│ 
├── theme/                     # Theme configuration to override bootstrap styles
├── requirements.txt
├── package.json
├── manage.py
├── db.sqlite3
└── README.md
```

## 🎨 Customization

### Fonts
The project uses **IBM Plex Sans** Font definitions are in [static/css/style.css](project/static/css/style.css).

### Styling
- Main stylesheet: [static/css/style.css](project/static/css/style.css)
- Compiled from SASS using `sass` package
- Bootstrap and custom CSS combined for responsive design

### Icons
SVG icons are used throughout the application.

### JavaScript Implementation
The JavaScript code that handles scroll detection is located in [templates/components/navbar.html](templates/components/navbar.html).



## For production deployment:
1. Change `DEBUG = False` in `project/settings.py`
2. Update `ALLOWED_HOSTS` with your domain


## 📦 Dependencies

### Python (Backend)
```
Django==6.0.3
sqlparse==0.5.5
asgiref==3.11.1
tzdata==2025.3
```

### JavaScript (Frontend)
```
bootstrap==5.3.8
sass==1.98.0
```