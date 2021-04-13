
from django.contrib import admin
from django.urls import path
from workshop.views import FrontPage
from django.views.decorators.csrf import csrf_exempt


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', csrf_exempt(FrontPage.as_view())),
]
