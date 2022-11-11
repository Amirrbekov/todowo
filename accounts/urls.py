from django.urls import path
from accounts.views import signupuser, signinuser, logoutuser

app_name = "account"

urlpatterns = [
    path('signup/', signupuser, name='signupuser'),
    path("signin/", signinuser, name='signinuser'),
    path("logout/", logoutuser, name="logoutuser" )
]
