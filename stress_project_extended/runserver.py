import os
import webbrowser
from threading import Timer

def open_browser():
    webbrowser.open("http://127.0.0.1:8000")

# Set Django settings module (INNER FOLDER NAME)
os.environ.setdefault(
    "DJANGO_SETTINGS_MODULE",
    "stress_project_extended.settings"
)

# Open browser after server starts
Timer(2, open_browser).start()

from django.core.management import execute_from_command_line

# Run Django server
execute_from_command_line([
    "manage.py",
    "runserver",
    "127.0.0.1:8000"
])

