from django.urls import path
from . import views

urlpatterns = [
    path('', views.sendMessage_view, name = 'contact'),
    path('confirm/', views.message_view, name = 'confirmation'),
]