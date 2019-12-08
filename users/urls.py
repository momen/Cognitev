from django.urls import path
from users.views import UserCreation, CustomAuthToken, ReAuthToken

app_name = "users"

urlpatterns = [

    path("register/", UserCreation.as_view()),
    path("token/", CustomAuthToken.as_view()),
    path("user_from_token/", ReAuthToken.as_view()),
]
