
from project.settings import *  # importa tudo do settings original

# Sobrescreve o DATABASES para usar SQLite em memória
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / "test_db.sqlite3",
    }
}
