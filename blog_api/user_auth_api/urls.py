from django.urls import path
from user_auth_api.views import HelloWorldView

urlpatterns = [
    path('home_page/', HelloWorldView.as_view(), name = "greetings"),
]
