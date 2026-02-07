<div align="center">

# 🌐 Network - Social Media Platform

[![Live Demo](https://img.shields.io/badge/demo-live-success?style=for-the-badge&logo=render)](https://network-social-media-platform.onrender.com/)
[![Django](https://img.shields.io/badge/Django-5.2.7-092E20?style=for-the-badge&logo=django)](https://www.djangoproject.com/)
[![Python](https://img.shields.io/badge/Python-3.8+-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![License](https://img.shields.io/badge/License-MIT-blue.svg?style=for-the-badge)](LICENSE)

**A modern, feature-rich social media platform built with Django**

Experience seamless social connectivity with real-time interactions, elegant UI, and robust functionality.

</div>

---

## 📋 Table of Contents

- [Overview](#overview)
- [Key Features](#key-features)
- [Tech Stack](#tech-stack)
- [Architecture](#architecture)
- [Local Setup](#local-setup)
- [Usage](#usage)
- [API Reference](#api-reference)
- [Security](#security)
- [License](#license)
- [Contact](#contact)
- [Acknowledgments](#acknowledgments)

---

## Overview

**Network** is a production-ready social media platform that enables users to connect, share, and engage with a vibrant community. Built with Django and modern web technologies, it delivers a seamless user experience with real-time interactions, secure authentication, and scalable architecture.

The platform is designed with best practices in mind, featuring clean code architecture, responsive design, and comprehensive user interaction capabilities that rival mainstream social media platforms.

## Key Features

### 🔐 Authentication & Security

- **Secure User Registration** - Robust validation with password encryption and strength requirements
- **Session Management** - Secure authentication with Django's battle-tested session framework
- **Custom User Model** - Extended user model for scalability and future feature additions
- **Protected Routes** - Authorization middleware ensuring secure access control
- **CSRF Protection** - Built-in protection against cross-site request forgery attacks

### 👥 User Profiles & Identity

- **Rich Profile System** - Customizable profiles with biography and avatar support
- **Profile Discovery** - Browse and explore user profiles across the network
- **Real-time Updates** - Dynamic profile editing with instant feedback
- **User Statistics** - Track followers, following, and post counts
- **Profile Validation** - Input sanitization and validation for data integrity

### 🔗 Social Network Features

- **Follow/Unfollow System** - Build connections with one-click follow functionality
- **Network Analytics** - View comprehensive follower and following lists
- **Relationship Tracking** - Real-time updates on connection status
- **AJAX-powered Interactions** - Seamless follow/unfollow without page reloads

### 📝 Content Management

- **Rich Post Creation** - Share content with titles and detailed descriptions
- **Full CRUD Operations** - Create, read, update, and delete posts with ease
- **Personalized Feed** - Smart feed showing content from followed users
- **Global Feed** - Discover new content from the entire community
- **Content Ownership** - Users maintain complete control over their posts
- **Timestamp Tracking** - Creation and modification timestamps for all content

### ❤️ Real-time Engagement

- **Real-time Like System** - AJAX-powered instant like/unlike functionality
- **Threaded Comments** - Engage in discussions with hierarchical comment structure
- **Comment Management** - Edit and delete comments with full version control
- **Interactive UI** - Dynamic updates without page refreshes

### 🎨 User Experience

- **Responsive Design** - Mobile-first approach ensuring compatibility across all devices
- **Intuitive Navigation** - Clean, user-friendly interface with logical flow
- **Fast Page Loads** - Optimized queries and efficient pagination
- **Error Handling** - Custom 404 pages and graceful error management
- **Accessibility** - Semantic HTML and ARIA labels for inclusivity

### ⚙️ Administrative Features

- **Comprehensive Admin Panel** - Django admin interface for platform management
- **User Moderation** - Tools for managing users and content
- **Analytics Dashboard** - Insights into platform usage and engagement
- **Content Moderation** - Review and manage reported content
- **System Configuration** - Flexible settings for platform customization

---

## Tech Stack

### Backend Framework

![Django](https://img.shields.io/badge/Django-5.2.7-092E20?style=flat-square&logo=django)
![Python](https://img.shields.io/badge/Python-3.8+-3776AB?style=flat-square&logo=python&logoColor=white)

- **Django 5.2.7** - High-level Python web framework for rapid development
- **Django ORM** - Powerful database abstraction layer for efficient queries
- **Django Admin** - Comprehensive admin interface out-of-the-box
- **Django Templates** - Server-side rendering with template inheritance

### Frontend Technologies

![HTML5](https://img.shields.io/badge/HTML5-E34F26?style=flat-square&logo=html5&logoColor=white)
![CSS3](https://img.shields.io/badge/CSS3-1572B6?style=flat-square&logo=css3&logoColor=white)
![JavaScript](https://img.shields.io/badge/JavaScript-F7DF1E?style=flat-square&logo=javascript&logoColor=black)

- **HTML5** - Semantic markup for accessibility and SEO
- **CSS3** - Modern styling with flexbox and grid layouts
- **JavaScript (Vanilla)** - Dynamic interactions and AJAX functionality
- **Responsive Design** - Mobile-first CSS for all screen sizes

### Database

![SQLite](https://img.shields.io/badge/SQLite-003B57?style=flat-square&logo=sqlite&logoColor=white)
![MySQL](https://img.shields.io/badge/MySQL-4479A1?style=flat-square&logo=mysql&logoColor=white)

- **SQLite** - Lightweight, serverless database for data persistence for local development
- **MySQL** - Scalable relational database for production environments
- **Migration System** - Version-controlled database schema management

### Deployment & Infrastructure

![Render](https://img.shields.io/badge/Render-Platform-46E3B7?style=flat-square&logo=render&logoColor=white)

- **Render** - Modern cloud platform for seamless deployment
- **Git** - Version control and deployment automation
- **WSGI** - Production-ready application server interface

### Development Tools

- **Django Validators** - Input validation and data sanitization
- **CSRF Middleware** - Security against cross-site request forgery
- **Session Framework** - Secure user session management

---

## Architecture

Network follows Django's MVT (Model-View-Template) architecture pattern with a modular app structure for maintainability and scalability.

### Application Structure

```
┌─────────────────────────────────────────┐
│          Django Project Layer           │
│         (network/settings.py)           │
└──────────────┬──────────────────────────┘
               │
       ┌───────┴───────┐
       │  URL Router   │
       │ (urls.py)     │
       └───────┬───────┘
               │
    ┌──────────┴──────────┐
    │                     │
┌───▼────┐         ┌──────▼──────┐
│ Views  │◄────────┤   Models    │
└───┬────┘         └──────┬──────┘
    │                     │
    │              ┌──────▼────────────┐
    │              │      Database     │
    │              │  (SQLite / MySQL) │
    │              └───────────────────┘
    │
┌───▼────────┐
│ Templates  │
└────────────┘
```

### Modular App Design

| App                | Responsibility                                           |
| ------------------ | -------------------------------------------------------- |
| **authenticate**   | User registration, login, and session management         |
| **users**          | Profile management, follow system, and user interactions |
| **feed_and_posts** | Post creation, feeds, comments, and engagement           |
| **core**           | Landing pages, about, contact, and static content        |
| **admincontrol**   | Administrative functionality and moderation              |

## Local Setup

### Prerequisites

Ensure you have the following installed on your system:

- **Python** 3.12 or higher ([Download](https://www.python.org/downloads/))
- **Git** ([Download](https://git-scm.com/downloads))
- **uv** (Python package manager)

### Installation

Follow these steps to set up the project locally:

#### 1️⃣ Clone the Repository

```bash
git clone https://github.com/krsahil8825/Network-social-media-platform.git
cd Network
```

#### 2️⃣ UV Environment Setup

```bash
uv sync
```

#### 3️⃣ Configure Environment Variables

Create a `.env` file in the project root (optional for local development):

```env
SECRET_KEY=dev-only-insecure-secret-key
ENV=development
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1
CSRF_TRUSTED_ORIGINS=http://localhost
DB_ENGINE=sqlite
```

#### 4️⃣ Apply Database Migrations

```bash
uv run python manage.py makemigrations
uv run python manage.py migrate
```

#### 5️⃣ Create Superuser (Admin Account)

```bash
uv run python manage.py createsuperuser
```

Follow the prompts to create your admin account.

#### 6️⃣ Run Development Server

```bash
uv run python manage.py runserver
```

#### 7️⃣ Access the Application

- **Main Application:** [http://localhost:8000](http://localhost:8000)
- **Admin Panel:** [http://localhost:8000/admin](http://localhost:8000/admin)

---

## Project Structure

```
Network/
│
├── 📂 authenticate/              # Authentication & Authorization
│   ├── views.py                  # Login, registration, logout views
│   ├── urls.py                   # Authentication routes
│   ├── templates/                # Auth-related templates
│   └── static/                   # Auth-specific CSS/JS
│
├── 📂 users/                     # User Profile Management
│   ├── models.py                 # Profile and Follow models
│   ├── views.py                  # Profile CRUD operations
│   ├── urls.py                   # Profile routes
│   ├── utils.py                  # Helper functions
│   ├── templates/                # Profile templates
│   └── static/                   # Profile-specific JS (follow.js)
│
├── 📂 feed_and_posts/            # Content & Engagement
│   ├── models.py                 # Post, Comment, Like models
│   ├── views.py                  # Feed, post, comment views
│   ├── feed_urls.py              # Feed-related routes
│   ├── post_urls.py              # Post-related routes
│   ├── templates/                # Feed and post templates
│   └── static/                   # JS for likes, comments
│
├── 📂 core/                      # Core Functionality
│   ├── views.py                  # Home, about, contact views
│   ├── urls.py                   # Core routes
│   ├── templates/                # Landing and static pages
│   └── static/                   # Global CSS and images
│
├── 📂 admincontrol/              # Admin Features
│   ├── views.py                  # Admin-specific views
│   └── admin.py                  # Django admin configuration
│
├── 📂 network/                   # Project Configuration
│   ├── settings.py               # Django settings
│   ├── urls.py                   # Root URL configuration
│   ├── wsgi.py                   # WSGI application
│   └── asgi.py                   # ASGI application
│
├── 📂 database/                  # Database Configuration
│   ├── docker-compose.yml        # Docker setup for DB
│   └── info.txt                  # Database information
│
├── 📂 other/                     # Utilities
│   ├── generateSecret.py         # Secret key generator
│   └── Important_commands.md     # Useful Django commands
│
├── 📄 manage.py                  # Django management script
├── 📄 db.sqlite3                 # SQLite database
├── 📄 requirements.txt           # Python dependencies
├── 📄 pyproject.toml             # Project metadata
├── 📄 README.md                  # Project documentation
└── 📄 LICENSE                    # MIT License
```

---

## Usage

### For End Users

#### Getting Started

1. **Create an Account**
    - Navigate to the registration page
    - Fill in username, email, and password
    - Verify your account and log in

2. **Set Up Your Profile**
    - Click on your username to view your profile
    - Click "Edit Profile" to add:
        - Profile biography
        - Avatar/profile picture
        - Other personal information

3. **Build Your Network**
    - Browse user profiles
    - Click "Follow" on profiles you're interested in
    - View your followers and following lists

4. **Create Content**
    - Click "Create Post" from the navigation menu
    - Add a compelling title and content
    - Publish to share with your network

5. **Engage with Content**
    - Browse your personalized feed of followed users
    - Like posts by clicking the heart icon
    - Add comments to start discussions
    - Edit or delete your own posts and comments

### For Administrators

#### Access Admin Panel

1. Navigate to `/admin` or click the admin link
2. Log in with superuser credentials
3. Access comprehensive management tools

#### Admin Capabilities

- **User Management**: View, edit, and moderate user accounts
- **Content Moderation**: Review and manage posts and comments
- **Statistical Overview**: Monitor platform activity and engagement
- **Permission Control**: Assign roles and permissions
- **System Configuration**: Modify platform settings

---

## API Reference

### Authentication Endpoints

| Endpoint          | Method | Description               |
| ----------------- | ------ | ------------------------- |
| `/auth/register/` | POST   | Register new user account |
| `/auth/login/`    | POST   | Authenticate user         |
| `/auth/logout/`   | POST   | End user session          |

### User Endpoints

| Endpoint                   | Method | Description          |
| -------------------------- | ------ | -------------------- |
| `/users/<username>/`       | GET    | View user profile    |
| `/users/edit/`             | POST   | Update user profile  |
| `/users/follow/<user_id>/` | POST   | Follow/unfollow user |

### Post Endpoints

| Endpoint                   | Method | Description            |
| -------------------------- | ------ | ---------------------- |
| `/feed/`                   | GET    | View personalized feed |
| `/feed/all/`               | GET    | View all posts         |
| `/posts/create/`           | POST   | Create new post        |
| `/posts/<post_id>/`        | GET    | View specific post     |
| `/posts/<post_id>/edit/`   | PUT    | Edit post              |
| `/posts/<post_id>/delete/` | DELETE | Delete post            |
| `/posts/<post_id>/like/`   | POST   | Like/unlike post       |

### Comment Endpoints

| Endpoint                         | Method | Description    |
| -------------------------------- | ------ | -------------- |
| `/posts/<post_id>/comment/`      | POST   | Add comment    |
| `/comments/<comment_id>/edit/`   | PUT    | Edit comment   |
| `/comments/<comment_id>/delete/` | DELETE | Delete comment |

---

## Security

Network implements multiple security measures to protect user data and ensure platform integrity:

### Implemented Security Features

✅ **Authentication & Authorization**

- Secure password hashing using Django's PBKDF2 algorithm
- Session-based authentication with secure cookies
- Login required decorators for protected views
- User permission checks for content modification

✅ **Data Protection**

- CSRF protection on all forms
- SQL injection prevention via Django ORM
- XSS protection through template escaping
- Input validation and sanitization

✅ **Production Security**

- HTTPS enforcement in production
- Secure cookie flags (HTTPOnly, Secure)
- Content Security Policy headers
- Protection against clickjacking

### Security Best Practices

```python
# Example security settings
SECURE_SSL_REDIRECT = True
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True
SECURE_BROWSER_XSS_FILTER = True
X_FRAME_OPTIONS = 'DENY'
SECURE_CONTENT_TYPE_NOSNIFF = True
```

### Reporting Security Issues

If you discover a security vulnerability, please email [krsahil8825@gmail.com](mailto:krsahil8825@gmail.com) with details. Do not create public GitHub issues for security vulnerabilities.

---

## Dependencies

I've used the following key dependencies:

- `Django==5.2.7` - Web framework
- `asgiref==3.10.0` - ASGI support
- `sqlparse==0.5.3` - SQL parsing
- `tzdata==2025.2` - Timezone data
- `validators==0.35.0` - Data validation
- `requests==2.32.5` - HTTP library

For complete list, see [pyproject.toml](pyproject.toml).

## License

I've licensed this project under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contact

I'd love to hear from you! For questions, feedback, or collaboration:

- **GitHub**: [krsahil8825](https://github.com/krsahil8825)
- **Email**: [krsahil8825@gmail.com](mailto:krsahil8825@gmail.com)

## Acknowledgments

I'd like to thank the Django community for the excellent framework and documentation that made this project possible.

**Made with ❤️ by Kumar Sahil**
