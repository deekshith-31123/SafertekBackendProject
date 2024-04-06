"""
URL configuration for file_server_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('upload/', views.upload_file, name='upload_file'),

    path('createFile/', views.create_file, name='create_file'),
    path('getFiles/', views.get_files, name='get_files'),
    path('getFile/<str:filename>/', views.get_file, name='get_file'),
    path('modify_file/<str:filename>/', views.modify_file_view, name='modify_file'),
    path('file_modified/', views.file_modified, name='file_modified'),
    path('delete_file/<str:filename>/', views.delete_file, name='delete_file'),
]
if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
from django.urls import path
from . import views



