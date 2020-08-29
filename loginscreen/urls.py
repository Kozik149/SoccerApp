from django.urls import path
from loginscreen import views


urlpatterns = [
    path('', views.login, name='login'),
]