import os
from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
from ifri_pi9_backend.routing import websocket_urlpatterns
from ifri_pi9_backend.msg.consumers import ChatConsumer

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ifri_pi9_backend.config.settings')

application = ProtocolTypeRouter({
    "http": get_asgi_application(),
    "websocket": AuthMiddlewareStack(
        URLRouter(
            websocket_urlpatterns
        )
    ),
})