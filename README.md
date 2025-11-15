# Network - A Minimal Social Media Platform Built with Django

**Network** is a lightweight social platform built with Django that demonstrates core social-media features such as posting, following, liking, and commenting.
This project is ideal for learners exploring Django, developers studying app architecture, or anyone looking for a clean base to extend.

## Features

### **Authentication (`authenticate` app)**

-   User registration with validation
-   Secure session-based login/logout
-   Templates: `login.html`, `register.html`

### **User Profiles & Following (`users` app)**

-   Profile view and edit pages
-   Follow/Unfollow with AJAX (`static/users/js/follow.js`)
-   “Following Feed” to display posts from followed users

### **Posts, Likes & Comments (`feed_and_posts` app)**

-   Create, edit, delete, and view posts
-   Comment system with validation
-   Like/Unlike functionality using AJAX (`static/feed_and_posts/js/like.js`)
-   Pagination for large feeds with reusable templates

### **Core Pages (`core` app)**

-   Static pages (About, Contact)
-   Shared layout with navbar and footer components

### **Admin Tools (`admincontrol` app)**

-   Custom admin page extensions and moderation utilities

## Architecture & Tech Stack

-   **Framework**: Django 5.2.x
-   **Database**: SQLite (default for development)
-   **Templates**: Organized per app
-   **Static Files**: JS/CSS stored inside each app’s `static/` directory

## Installation (Windows / PowerShell)

1. **Create and activate a virtual environment**

```powershell
python -m venv .venv; .\.venv\Scripts\Activate.ps1
```

2. **Install dependencies**

```powershell
python -m pip install --upgrade pip
pip install -r requirements.txt
```

3. **Apply migrations & create superuser (optional)**

```powershell
python manage.py migrate
python manage.py createsuperuser
```

4. **Start the development server**

```powershell
python manage.py runserver
```

Open the site at: **[http://127.0.0.1:8000/](http://127.0.0.1:8000/)**

## Running Tests

Execute the full test suite:

```powershell
python manage.py test
```

### Test coverage includes:

-   Authentication (login, registration, invalid input handling)
-   Authorization rules (only owners can edit/delete posts)
-   Post CRUD operations
-   Follow/Unfollow logic with idempotency checks
-   Like system and duplicate prevention
-   Comment validation
-   Pagination boundaries and empty feed handling

## Defensive & Robust Behavior

-   Server-side form validation on all user input
-   Ownership and authentication checks for sensitive actions
-   Idempotent like/follow endpoints
-   Template auto-escaping for XSS safety
-   Graceful handling of pagination edge-cases

## Continuous Integration (GitHub Actions)

Workflow found at: `/.github/workflows/test.yaml`

What it does:

-   Installs dependencies
-   Runs full Django test suite on every push/PR to `main`
-   Ensures only passing code is merged

## Project Structure

```
/manage.py
/requirements.txt
/db.sqlite3
/README.md

/network/                  # Django project config
/authenticate/             # Login & registration
/users/                    # Profiles, follow system
/feed_and_posts/           # Posts, likes, comments, feeds
/core/                     # Static pages, shared layout
/admincontrol/             # Admin utilities
/static/                   # JS/CSS per app
/templates/                # Organized by app
/.github/workflows/        # CI configuration
```

## Contributing

1. Fork the repository
2. Create a feature branch
3. Add or update tests if needed
4. Submit a pull request

Follow Django conventions for project layout and naming.

## License & Contact

-   **License**: MIT
-   **Author**: Kumar Sahil
-   **Email**: [krsahil8825@gmail.com](mailto:krsahil8825@gmail.com)
