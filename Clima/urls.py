from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('login.urls')),
    path('cadastro/', include('cadastro.urls')),
    path('dashboard/', include('dashboard.urls')),
]
