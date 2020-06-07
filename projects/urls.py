from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

app_name = 'projects'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('profile/<int:profile_id>', views.user_profile, name='profile'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
