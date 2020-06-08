from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

app_name = 'projects'

urlpatterns = [
    path('', views.index, name='index'),
    path('profile/<int:profile_id>', views.user_profile, name='profile'),
    path('add_project', views.add_project, name='add_project'),
    path('search', views.search_by_project_title, name='search_results'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
