# Django Job Board

A full-featured job board application built with Django that connects job seekers with companies. The platform allows companies to post job openings and manage applications, while users can browse jobs and apply with their details.

## 🚀 Features

### For Job Seekers (Users)
- **User Registration & Authentication**: Secure signup and login with encrypted passwords
- **Browse Jobs**: View all available job listings with search functionality
- **Job Details**: View comprehensive information about each job posting
- **Apply to Jobs**: Submit applications with personal details, resume, cover letter, and LinkedIn profile
- **Password Recovery**: Reset forgotten passwords via email OTP verification

### For Companies
- **Company Registration & Authentication**: Separate registration and login system for companies
- **Company Dashboard**: Dedicated home page for managing company activities
- **Post Jobs**: Create new job listings with title, required skills, and job type
- **Manage Jobs**: View, update, and delete posted jobs
- **View Applications**: Review all applications submitted for each job posting
- **Password Recovery**: Reset forgotten passwords via email OTP verification

## 📋 Prerequisites

Before running this project, ensure you have the following installed:
- Python 3.8 or higher
- pip (Python package installer)
- Django 5.0.6 or compatible version

## 🛠️ Installation

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd jobBoard
   ```

2. **Create a virtual environment** (recommended)
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install django
   ```

4. **Configure Email Settings**
   
   Update the email configuration in `jobs/views.py` for OTP functionality:
   - Set up your SMTP server credentials
   - Configure sender email and app password
   - **Note**: Never commit sensitive credentials to version control

5. **Apply database migrations**
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

6. **Create a superuser** (for admin access)
   ```bash
   python manage.py createsuperuser
   ```

7. **Run the development server**
   ```bash
   python manage.py runserver
   ```

8. **Access the application**
   - Open your browser and navigate to `http://127.0.0.1:8000/`
   - Admin panel: `http://127.0.0.1:8000/admin/`

## 📁 Project Structure

```
jobBoard/
│
├── jobBoard/                 # Main project directory
│   ├── __init__.py
│   ├── asgi.py              # ASGI configuration
│   ├── settings.py          # Project settings
│   ├── urls.py              # Main URL configuration
│   └── wsgi.py              # WSGI configuration
│
├── jobs/                     # Main application
│   ├── migrations/          # Database migrations
│   ├── __init__.py
│   ├── admin.py             # Admin panel configuration
│   ├── apps.py              # App configuration
│   ├── models.py            # Database models
│   ├── urls.py              # App URL patterns
│   ├── views.py             # View functions
│   └── tests.py             # Test cases
│
├── templates/               # HTML templates
│   ├── userLogin.html       # User login page
│   ├── userRegister.html    # User registration page
│   ├── userHome.html        # User home page
│   ├── companyLogin.html    # Company login page
│   ├── companyRegister.html # Company registration page
│   ├── companyHome.html     # Company dashboard
│   ├── jobs.html            # Job listings page
│   ├── detail.html          # Job detail page
│   ├── userform.html        # Job application form
│   ├── jobCreate.html       # Create job form
│   ├── jobsCompany.html     # Company's job listings
│   ├── update.html          # Update job form
│   ├── application.html     # View applications
│   ├── forgotPasswordUser.html      # User password recovery
│   └── forgotPasswordCompany.html   # Company password recovery
│
├── static/                  # Static files (CSS, JS, images)
├── db.sqlite3              # SQLite database
└── manage.py               # Django management script
```

## 🗄️ Database Models

### Job
- `sno`: Primary key (auto-increment)
- `Company`: Company name (max 50 characters)
- `Job_title`: Job title (max 100 characters)
- `Skills_required`: Required skills (text field)
- `Job_type`: Type of job (max 30 characters)

### Application
- `full_name`: Applicant's full name
- `email`: Applicant's email address
- `phone`: Contact number
- `position`: Applied position
- `resume`: Resume file upload
- `cover_letter`: Cover letter text
- `linkedin`: LinkedIn profile URL (optional)
- `submitted_at`: Timestamp of submission
- `job`: Foreign key to Job (integer reference)

### User
- `name`: User's name
- `email`: User's email address
- `password`: Encrypted password

### Company
- `name`: Company name
- `email`: Company email address
- `password`: Encrypted password

## 🔐 Security Features

- **Password Encryption**: All passwords are hashed using Django's `make_password` function
- **Password Verification**: Secure password checking with `check_password`
- **OTP Verification**: Two-factor authentication for password recovery
- **Session Management**: Secure session handling for OTP and user data
- **CSRF Protection**: Built-in Django CSRF middleware

## 🌐 URL Routes

### User Routes
- `/` - User login page
- `/userReg/` - User registration
- `/userHome/` - User home page
- `/jobs/` - Browse all jobs with search
- `/jobs/<slug>` - Job details
- `/job/apply/<company>/<title>/<id>` - Job application form
- `/forgot-password/user/` - User password recovery

### Company Routes
- `/companyLogin/` - Company login page
- `/companyReg/` - Company registration
- `/companyHome/<company_name>` - Company dashboard
- `/job/create/<company_name>` - Create new job
- `/job/list/<company_name>` - View company's jobs
- `/update/<id>/<company>/<title>/<skills>/<type>/` - Update job
- `/delete/<id>/<company>` - Delete job
- `/applications/<job_id>/` - View job applications
- `/forgot-password/company/` - Company password recovery

### Admin Route
- `/admin/` - Django admin panel

## 🎨 Features Breakdown

### Authentication System
- Separate login systems for users and companies
- Email-based registration
- Duplicate email validation
- Password encryption and validation

### Job Management
- Create, Read, Update, Delete (CRUD) operations
- Search functionality for job listings
- Detailed job view with company information
- Job categorization by type

### Application System
- Resume upload capability
- Cover letter submission
- LinkedIn profile integration
- Application tracking by job posting
- Timestamp for submission tracking

### Password Recovery
- OTP generation and email delivery
- Session-based OTP verification
- Secure password reset flow
- Separate recovery flows for users and companies

## 🔧 Configuration Notes

### Email Configuration
The application uses SMTP for sending OTP emails. You'll need to configure:
- SMTP server (currently using Gmail's SMTP)
- Sender email address
- App-specific password or authentication token

**Important**: Store email credentials securely using environment variables or Django's secrets management.

### File Uploads
- Resume files are uploaded to the `resumes/` directory
- Ensure proper media file configuration in `settings.py`
- Set up `MEDIA_ROOT` and `MEDIA_URL` for production

## 📝 Admin Panel

The Django admin panel provides an interface to:
- Manage all jobs
- View and filter applications
- Manage user accounts
- Manage company accounts
- Perform bulk operations

Access the admin panel with superuser credentials at `/admin/`.

## 🚀 Deployment Considerations

Before deploying to production:

1. **Security Settings**
   - Set `DEBUG = False` in `settings.py`
   - Configure `ALLOWED_HOSTS`
   - Use environment variables for sensitive data
   - Generate a new `SECRET_KEY`

2. **Database**
   - Consider migrating from SQLite to PostgreSQL/MySQL
   - Set up regular database backups

3. **Static Files**
   - Configure static file serving
   - Run `python manage.py collectstatic`

4. **Media Files**
   - Set up proper file storage (e.g., AWS S3)
   - Configure file upload limits

5. **Email**
   - Use production email service
   - Implement proper error handling for email failures

## 🤝 Contributing

Feel free to fork this repository and submit pull requests. For major changes, please open an issue first to discuss proposed changes.

## 📄 License

This project is open-source and available for educational purposes.

## 📧 Support

For questions or issues, please open an issue in the repository or contact the development team.

---

**Note**: This is a development version. Ensure proper security measures and testing before deploying to production.
