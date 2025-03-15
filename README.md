# Customer Relationship Manager (CRM)

A full-featured Django-based Customer Relationship Management system designed to help businesses manage customer interactions and data.

## Overview

This Customer Relationship Manager is a web application built with Django and MySQL that allows users to:
- Store and manage customer records
- Track customer information (contact details, addresses, etc.)
- Register and authenticate users
- Manage user permissions

## Features

- **User Authentication**: Secure login and registration system
- **Record Management**: Add, view, update, and delete customer records
- **Responsive Design**: Mobile-friendly interface built with Bootstrap
- **User-friendly Interface**: Clean and intuitive UI for easy navigation

## Tech Stack

- **Backend**: Django 5.1+
- **Database**: MySQL
- **Frontend**: HTML, CSS, Bootstrap 5
- **Authentication**: Django Authentication System

## Installation and Setup

### Prerequisites

- Python 3.8+
- MySQL
- pip

### Step 1: Clone the Repository

```bash
git clone https://github.com/yourusername/customerRelationshipManager.git
cd customerRelationshipManager
```

### Step 2: Set Up a Virtual Environment (Optional but Recommended)

```bash
python -m venv venv
source venv/bin/activate  # On Windows, use: venv\Scripts\activate
```

### Step 3: Install Dependencies

```bash
pip install -r requirements.txt
```

### Step 4: Create MySQL Database

Run the database creation script:

```bash
python dcrm/mydb.py
```

This will create a MySQL database named "rewire".

### Step 5: Configure Database Settings

The database settings are already configured in `dcrm/dcrm/settings.py`, but you might need to update them if your MySQL setup differs:

```python
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.mysql",
        "NAME": "rewire",
        "USER": "root",
        "PASSWORD": "your_mysql_password",
        "HOST": "localhost",
        "PORT": '3306'
    }
}
```

### Step 6: Run Migrations

```bash
cd dcrm
python manage.py migrate
```

### Step 7: Create a Superuser (Admin)

```bash
python manage.py createsuperuser
```

### Step 8: Run the Development Server

```bash
python manage.py runserver
```

The application will be available at http://127.0.0.1:8000/

## Usage

### Login/Registration
- New users can register by clicking the "Signup" link in the navigation bar
- Existing users can log in from the home page

### Managing Records
Once logged in, you can:
- View all customer records from the home page
- Add new records by clicking "Add Record" in the navigation bar
- View detailed information for any record by clicking "view"
- Update or delete records from the detail view

### Admin Interface
Access the Django admin interface at http://127.0.0.1:8000/admin/ to manage the application at an administrative level.

## Security Notice

The current configuration includes the Django secret key in the settings file. For production use:
- Generate a new secret key
- Store the key as an environment variable
- Set DEBUG = False
- Update ALLOWED_HOSTS

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contributing

Contributions are welcome! Feel free to fork the repository and submit pull requests.

## Author

Yasith Gunawardhana
