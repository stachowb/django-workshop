
from django.contrib import admin
from django.urls import path
from workshop.views import Home, ListRoom, RoomAdd, DeleteRoom, EditRoom, ViewRoom, ListReservation, AddReservation
from django.views.decorators.csrf import csrf_exempt


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', Home.as_view(), name="home"),
    path('rooms/', ListRoom.as_view(), name="room_list"),
    path('rooms/add/', RoomAdd.as_view(), name="room_add"),
    path('rooms/delete/<int:room_id>/', DeleteRoom.as_view(), name='room_delete'),
    path('rooms/edit/<int:room_id>/', EditRoom.as_view(), name='room_edit'),
    path('rooms/view/<int:room_id>/', ViewRoom.as_view(), name='room_view'),
    path('reservations/', ListReservation.as_view(), name="reservations_list"),
    path('reservations/add/', AddReservation.as_view(), name="reservations_add")


]
