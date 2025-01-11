# Task Manager API
## Setup Instructions
1. **Clone the repository** :
   git clone <URL_TO_YOUR_REPOSITORY>
   cd task_manager

2. Create a virtual environment and activate it :
    python3 -m venv env
    source env/bin/activate

3. Install the dependencies :
    pip install -r requirements.txt

4. Run the migrations :
    python manage.py migrate
5. Start the development server :
    anage.py runserver
6. Project Structure
    taskmanager/ : Main project directory.
    tasks/ : Application directory.
    env/ : Virtual environment directory (excluded from version control).
    requirements.txt : List of dependencies.
    .gitignore : Git ignore file.
    ERD diagram.PNG
7. Model
![database models and relationships](<ERD diagram.png>)