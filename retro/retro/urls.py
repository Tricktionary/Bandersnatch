from django.contrib import admin
from django.urls import path, get_resolver

from core.views import home_page

urlpatterns = [
    path('',home_page.home_page, name="Home"),
    path('admin/', admin.site.urls),
]
