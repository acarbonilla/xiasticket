import os

from django.core.asgi import get_asgi_application
from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter

import baseApp.routing

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ticketingSystem.settings')

application = ProtocolTypeRouter({
    "http": get_asgi_application(),
    "websocket": AuthMiddlewareStack(
        URLRouter(
            baseApp.routing.websocket_urlpatterns
        )
    )
})
