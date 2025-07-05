# conftest.py
import pytest
from django.conf import settings
from django.core.management import call_command


@pytest.fixture(scope='session')
def django_db_setup(django_db_blocker):
    """
    Usa SQLite in-memory e aplica todas as migrations antes de rodar testes.
    """
    # Desbloqueia acesso a settings e comandos de management
    with django_db_blocker.unblock():
        # Sobrescreve o banco
        settings.DATABASES['default'] = {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': ':memory:',
        }
        # Aplica migrations (inclui criação de auth_user, etc)
        call_command('migrate', verbosity=0, interactive=False)
