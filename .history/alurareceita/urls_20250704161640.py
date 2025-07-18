from django.contrib import admin
from django.urls import path. inc

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('blog.urls'))
]
