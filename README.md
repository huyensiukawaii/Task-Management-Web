# TaskManabu

## Table of Contents
- [Introduction](#introduction)
- [Features](#features)
- [Tech Stack](#tech-stack)
- [Installation](#installation)
- [Usage](#usage)
- [Testing](#testing)
- [Demo](#demo)
## Introduction
TaskManabu is a web-based application designed to help users manage their tasks efficiently. This application provides a simple yet powerful interface to create, track, and complete tasks, enhancing productivity and organization.

## Features
- **User Authentication:** Secure user registration and login system.
- **Task Creation:** Add, edit, and delete tasks.
- **Priority Levels:** Assign priority levels to tasks and able to search tasks by priority levels.
- **Responsive Design:** Fully responsive design that works on all devices.

## Tech Stack
- **Frontend:** HTML, CSS, JavaScript, Bootstrap
- **Backend:** Django, Python
- **Database:** SQLite (default)
- **Other Tools:** Django Crispy Forms, Django Rest Framework

## Installation
Follow these steps to get a local copy of the project up and running:

1. **Clone the repository:**
    ```bash
    git clone https://github.com/PhucNgo5903/Task_Management_Web.git
    cd Task_Management_Web
    ```

2. **Create and activate a virtual environment:**
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
    ```

3. **Install the required packages:**
   ```bash
    pip install django
   ```
   ```bash
    pip install django-crispy-forms
   ```
   ```bash
    pip install crispy-bootstrap4
   ```
   ```bash
    pip install Pillow
   ```
   
5. **Run database migrations:**
    ```bash
    python manage.py migrate
    ```

6. **Create a superuser:**
    ```bash
    python manage.py createsuperuser
    ```

7. **Start the development server:**
    ```bash
    python manage.py runserver
    ```

## Usage
Once the server is running, open your web browser and navigate to `http://127.0.0.1:8000/`. Log in with your credentials to start managing your tasks.


## Testing
To run the tests, use the following command:
```bash
python manage.py test
```

Thank you for checking out TaskManabu! Happy task managing!


## DEMO:

Home page:
![Home page](https://github.com/user-attachments/assets/29b7b5f7-5992-40d9-96a5-08b83833d283)

Registration page
![Registration page](https://github.com/user-attachments/assets/2abf9fa9-3155-458c-83a5-1488b38bcdce)

Login page
![Login page](https://github.com/user-attachments/assets/8d51eed4-c306-44bc-8316-41b9c2ac622f)

Dashboard
![Dashboard](https://github.com/user-attachments/assets/118a73ee-872b-45cc-a503-adc47feb62ba)

Profile management
![Profile managment](https://github.com/user-attachments/assets/f98f1ad9-6c51-4dce-9b07-e216173e8064)

Create task
![Create task](https://github.com/user-attachments/assets/2cbbadbd-5e81-48f5-8844-60a8bc6f5b4e)

View tasks
![View tasks](https://github.com/user-attachments/assets/11da92e5-d339-4851-919a-4b55fc6389a0)

Update task
![Update task](https://github.com/user-attachments/assets/d6267b14-738b-4ca7-9b1c-07acaf69347c)

Delete task
![Delete task](https://github.com/user-attachments/assets/954d6d87-7def-4851-9e97-0bac61bd3940)






















