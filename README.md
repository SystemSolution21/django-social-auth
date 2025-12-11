# Django Social Authentication Example

This is a sample Django project demonstrating how to implement social authentication using the powerful `django-allauth` library. It is pre-configured for social login with **Google** and **GitHub**.

## Features

- User sign-in and sign-up using Google and GitHub.
- Custom templates to override `django-allauth`'s default look and feel.
- Secure handling of authentication tokens and user sessions.
- A clean, minimal setup that's easy to understand and build upon.

## Project Structure

```project-root
django-social-auth/
├── social_auth_app/      # Main Django project configuration
│   ├── settings.py
│   └── urls.py
├── templates/            # Project-wide templates
│   ├── social_auth_app/
│   │   ├── _base.html    # Base template with Bootstrap
│   │   └── home.html     # Home page
│   └── socialaccount/
│       └── login.html    # Custom confirmation page for social login
└── manage.py
```

## Getting Started

Follow these instructions to get a copy of the project up and running on your local machine for development and testing.

### Prerequisites

- Python 3.8+
- Pip (Python package installer)

### Installation

1. **Clone the repository:**

    ```sh
    git clone <your-repository-url>
    cd django-social-auth
    ```

2. **Create and activate a virtual environment:**

    ```sh
    # For Windows
    python -m venv venv
    .\venv\Scripts\activate

    # For macOS/Linux
    python3 -m venv venv
    source venv/bin/activate
    ```

3. **Install dependencies:**
    *(Note: A `requirements.txt` file should be created for a real project. For now, you can install `django-allauth` manually.)*

    ```sh
    pip install django "django-allauth>=0.58"
    ```

4. **Configure Social Applications:**
    - You will need API credentials (Client ID and Client Secret) from Google and GitHub.
        - **Google:** Create credentials in the Google Cloud Console.
        - **GitHub:** Create a new OAuth App in your GitHub Developer settings.
    - Run the server (`python manage.py runserver`) and navigate to the Django admin panel at `http://127.0.0.1:8000/admin/`.
    - Go to **Social Applications** and add a new application for both Google and GitHub, pasting in your Client ID and Secret for each. Ensure you select the correct site.

5. **Apply database migrations:**

    ```sh
    python manage.py migrate
    ```

6. **Run the development server:**

    ```sh
    python manage.py runserver
    ```

    The application will be available at `http://127.0.0.1:8000/`.

## License

This project is licensed under the MIT License - see the LICENSE.txt file for details.
