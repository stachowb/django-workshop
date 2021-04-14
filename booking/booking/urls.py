
from django.contrib import admin
from django.urls import path
from workshop.views import FrontPage, DeleteRoom, EditRoom, ViewRoom
from django.views.decorators.csrf import csrf_exempt


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', FrontPage.as_view(), name="home"),
    path('delete/<int:room_id>/', DeleteRoom.as_view(), name='delete'),
    path('edit/<int:room_id>/', EditRoom.as_view(), name='edit'),
    path('view/<int:room_id>/', ViewRoom.as_view(), name='view'),


]
