import os

from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter


#configured asgi to work with django channels
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')

application = ProtocolTypeRouter({
    'http': get_asgi_application()
})
