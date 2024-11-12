from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('accounts/login/', views.login_view, name="login"),
    path('accounts/register', views.register, name="register"),
    path('employee/<str:employee_name>/', views.employee_details,name="name")
    
]





#media handler

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    