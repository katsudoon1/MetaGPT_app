import os

from django.core.wsgi import get_wsgi_application
from django.urls import include, path

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'poker_platform.settings')

application = get_wsgi_application()

urlpatterns = [
    path('api/', include('api.urls')),
]

if __name__ == '__main__':
    from django.core.management import execute_from_command_line

    execute_from_command_line()
