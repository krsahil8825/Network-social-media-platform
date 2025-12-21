# Network - Social Media Platform

A modern, feature-rich social media platform built with Django. I've created Network to provide users with a seamless experience for connecting, sharing, and engaging with their community.

## Overview

Network is a full-featured social media application that enables users to create profiles, share posts, engage with content through likes and comments, and build meaningful connections by following other users. The platform prioritizes user experience, security, and scalability.

## Features

### 🔐 Authentication & Authorization

-   **User Registration**: I've implemented a secure registration system with validation and password protection
-   **Login System**: Secure authentication mechanism with session management
-   **Custom User Model**: Extends Django's built-in user model for flexibility and future scalability
-   **Protected Routes**: Ensure only authenticated users can access sensitive features

### 👥 User Profiles

-   **Profile Management**: I enable users to create and customize their profiles with bio and avatar
-   **Profile Viewing**: Browse other users' profiles and view their contributions
-   **Profile Editing**: Users can update their information easily through an intuitive interface

### 🔗 Social Connections

-   **Follow System**: I've implemented a robust follow/unfollow feature to build user networks
-   **Follower/Following Lists**: Track connections and view user networks
-   **Relationship Management**: Seamless interface to manage social connections

### 📝 Posts & Content

-   **Create Posts**: Users can share thoughts and content with title and detailed content
-   **Edit Posts**: I allow users to modify their posts after creation
-   **Delete Posts**: Users maintain full control over their content
-   **Post Feed**: I've created a personalized feed showing posts from users you follow
-   **All Posts Feed**: Browse the complete network feed with pagination

### ❤️ Engagement Features

-   **Like System**: I've implemented real-time like functionality for posts with AJAX
-   **Comment on Posts**: Users can engage in discussions through post comments
-   **Edit Comments**: Modify comments after posting
-   **Delete Comments**: Remove unwanted comments with full control

### 🎯 Additional Features

-   **Admin Control Panel**: I provide administrative capabilities for platform management
-   **About Section**: Information about the platform
-   **Contact Page**: Users can reach out for support or feedback
-   **Responsive Design**: I've ensured the platform works seamlessly across all devices
-   **Pagination**: Efficient content loading with paginated feeds
-   **404 Error Handling**: User-friendly error pages for better experience

## Tech Stack

### Backend

-   **Django 5.2.7**: Modern Python web framework
-   **Python**: Core language for backend development
-   **SQLite**: Database for data persistence

### Frontend

-   **HTML5**: Semantic markup structure
-   **CSS3**: Responsive and modern styling
-   **JavaScript**: Dynamic client-side interactions

### Tools & Libraries

-   **Django Admin**: Built-in admin interface for management
-   **Django ORM**: Database abstraction layer
-   **Django Templates**: Server-side template rendering

## Installation

### Prerequisites

-   Python 3.8 or higher
-   pip (Python package manager)
-   Virtual environment support

### Setup Instructions

1. **Clone the Repository**

    ```bash
    git clone https://github.com/krsahil8825/Network-social-media-platform.git
    cd Network
    ```

2. **Create Virtual Environment**

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
    ```

3. **Install Dependencies**

    ```bash
    pip install -r requirements.txt
    ```

4. **Run Migrations**

    ```bash
    python manage.py migrate
    ```

5. **Create Superuser (Admin)**

    ```bash
    python manage.py createsuperuser
    ```

6. **Start Development Server**

    ```bash
    python manage.py runserver
    ```

7. **Access the Application**
    - Main Application: `http://localhost:8000`
    - Admin Panel: `http://localhost:8000/admin`

## Project Structure

```
Network/
├── authenticate/          # User authentication and registration
├── core/                  # Core application with about and contact
├── feed_and_posts/        # Posts, comments, and feed management
├── users/                 # User profiles and social connections
├── admincontrol/          # Admin functionality
├── network/               # Project settings and configuration
├── static/                # CSS, JavaScript, and images
├── templates/             # HTML templates
├── db.sqlite3             # SQLite database
├── manage.py              # Django management script
└── requirements.txt       # Python dependencies
```

## Usage Guide

### For Users

1. **Register & Login**: Create an account and log in to the platform
2. **Complete Your Profile**: Add a bio and avatar to personalize your profile
3. **Start Following**: Discover and follow other users to build your network
4. **Create Posts**: Share your thoughts with meaningful titles and content
5. **Engage**: Like posts and comment on content from others
6. **Manage Content**: Edit or delete your posts and comments anytime

### For Administrators

-   Access the admin panel at `/admin`
-   Manage users, posts, comments, and platform settings
-   Monitor user activity and ensure community guidelines

## Dependencies

I've used the following key dependencies:

-   `Django==5.2.7` - Web framework
-   `asgiref==3.10.0` - ASGI support
-   `sqlparse==0.5.3` - SQL parsing
-   `tzdata==2025.2` - Timezone data
-   `validators==0.35.0` - Data validation
-   `requests==2.32.5` - HTTP library

For complete list, see [requirements.txt](requirements.txt).

## Future Enhancements

I'm planning to add the following features:

-   **Direct Messaging**: Private communication between users
-   **Notifications**: Real-time updates for user interactions
-   **Search Functionality**: Discover users and posts easily
-   **Trending Tags**: Popular content discovery
-   **Media Upload**: Support for images and videos in posts
-   **User Recommendations**: Personalized friend suggestions
-   **Dark Mode**: Enhanced user interface options

## Contributing

I welcome contributions to make Network better! If you have suggestions or improvements:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

I've licensed this project under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contact

I'd love to hear from you! For questions, feedback, or collaboration:

-   **GitHub**: [krsahil8825](https://github.com/krsahil8825)
-   **Email**: [krsahil8825@gmail.com](mailto:krsahil8825@gmail.com)

## Acknowledgments

I'd like to thank the Django community for the excellent framework and documentation that made this project possible.

**Made with ❤️ by Kumar Sahil**
