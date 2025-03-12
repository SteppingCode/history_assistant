from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from core.views import search, chat_bot, home

urlpatterns = [
    path('admin/', admin.site.urls),
    path('search/', search, name='search'),
    path('chat/', chat_bot, name='chat_bot'),
    path('', home, name='home'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)