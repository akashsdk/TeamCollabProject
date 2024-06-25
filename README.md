# TeamCollabProject

TeamCollabProject is a Django-based project management application.

## Prerequisites

- Python 3.x
- pip

## Setup Instructions

1. **Clone the Repository**:
    ```bash
    git clone https://github.com/yourusername/TeamCollabProject.git
    cd TeamCollabProject
    ```

2. **Create and Activate a Virtual Environment**:
    ```bash
    python3 -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
    ```

3. **Install Dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

4. **Create and Apply Migrations**:
    ```bash
    python3 manage.py makemigrations
    python3 manage.py migrate
    ```

5. **Create a Superuser**:
    ```bash
    python3 manage.py createsuperuser
    ```

6. **Run the Development Server**:
    ```bash
    python3 manage.py runserver
    ```

Access the application at `http://127.0.0.1:8000/` and the admin interface at `http://127.0.0.1:8000/admin/`.

## License

This project is licensed under the MIT License.
