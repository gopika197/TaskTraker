# TaskTraker
Introduction
TaskTracker is a simple Django web application designed for tracking tasks. It allows users to manage tasks with titles, descriptions, and completion statuses. The application also includes user management features for super admin users.

Features
Task Management:

Add new tasks with titles, descriptions, and completion status.
View a list of tasks with the ability to filter by completion status.
Edit existing tasks to update titles, descriptions, and completion status.
User Management:

Create new users with email addresses and passwords.
Delete users.
Change passwords for existing users.
Review user details, including email addresses and super admin status.
Task List View:

Display a list of all tasks on the homepage ("/tasks/").
Tasks are presented in a tabular format, showing titles, descriptions, and completion status.
Task Completion Toggle:

Implement a feature to mark tasks as completed or incomplete.
Users can toggle the completion status of a task by clicking a button on the task list page.
Access Control:

The task list page ("/tasks/") is accessible to all users, even those who are not logged in.
Prerequisites
Ensure you have the following installed on your machine:

Python (3.6 or higher)
Django
Installation
download the zipfile or clone the repository:
download the zipfile and extract the files
Navigate to the project directory:

cd TaskTracker
Create a virtual environment (recommended):

python -m venv venv
Activate the virtual environment:

On Windows:

venv\Scripts\activate
On macOS and Linux:

source venv/bin/activate
Install the required dependencies:
pip install -r requirements.txt

Run migrations:
python manage.py migrate

Usage
Create a superuser for admin access:


python manage.py createsuperuser
Start the development server:

python manage.py runserver
Access the admin interface at http://127.0.0.1:8000/admin/ and log in with the superuser credentials.

Access the TaskTracker application at http://127.0.0.1:8000/tasks/.
