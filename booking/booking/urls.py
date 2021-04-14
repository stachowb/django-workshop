
from django.contrib import admin
from django.urls import path
from workshop.views import FrontPage, DeleteRoom
from django.views.decorators.csrf import csrf_exempt


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', FrontPage.as_view(), name="home"),
    path('delete/<int:room_id>/', DeleteRoom.as_view(), name='delete'),

]
