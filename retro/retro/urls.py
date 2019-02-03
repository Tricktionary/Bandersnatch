from django.contrib import admin
from django.urls import path, get_resolver

from core.views import home_page
from core.views import signup
from core.views import login 
from core.views import stage

urlpatterns = [
    
    path('admin/', admin.site.urls),

    path('',home_page.home_page, name="Home"),

    path('login/',login.login_page,name="Login Page"),
    path('login/submit/',login.login_submit,name="Login Submit"),
    path('signup/',signup.signup_page,name="Signup Page"),
    path('signup/submit/',signup.signup_submit,name="Signup Submit"),
    path('stage/',stage.stage,name="Stage")
]
