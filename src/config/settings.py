from pathlib import Path
from split_settings.tools import include

BASE_DIR = Path(__file__).resolve().parent.parent.parent

include(
    "security.py",
    "apps.py",
    "middleware.py",
    "templates.py",
    "database.py",
    "i18n.py",
    "auth.py",
    "static.py",
)



