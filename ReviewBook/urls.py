from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from accounts.views import registration_view, login_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('movies/', include('movies.urls')),
    path('games/', include('games.urls')),
    path('series/', include('series.urls')),
    path('', include('base.urls')),
    path('', include('accounts.urls')),
    path('oauth/', include('social_django.urls', namespace='social')),
    path('register/', registration_view, name="register"),
    path('login/', login_view, name="login"),
]

if settings.DEBUG:
    urlpatterns +=static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns +=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

