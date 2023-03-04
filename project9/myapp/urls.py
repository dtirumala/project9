
from django.urls import path
from myapp import views
urlpatterns = [
    
    path('log',views.login),
    path('logdata',views.read_logdata),
    
]