from django.shortcuts import render, redirect
from django.http import Http404, HttpResponse
from django.views import View
from django.views.generic.edit import DeleteView
from workshop.models import Room, Reservations
from django.contrib import messages


class Home(View):
    def get(self, request):
        return render(request, "base.html")


class RoomAdd(View):
    def get(self, request):
        return render(request, "room_add.html")

    def post(self, request):
        room = Room.objects.create()
        if name := request.POST.get('name'):
            room.name = name
        if capacity := request.POST.get('cap'):
            room.capacity = int(capacity)
        if request.POST.get('proj'):
            room.projector = True
        if capacity and name:
            room.save()
            return redirect("room_list")
        return redirect("room_add")


class DeleteRoom(View):

    def get(self, request, room_id):
        return render(request, "room_delete.html")

    def post(self, request, room_id):
        if request.POST.get('confirm'):
            room = Room.objects.get(id=room_id)
            room.delete()
        return redirect("room_list")


class EditRoom(View):
    def get(self, request, room_id):
        room = Room.objects.get(id=room_id)
        return render(request, 'room_edit.html', {"room": room})

    def post(self, request, room_id):
        room = Room.objects.get(id=room_id)
        if request.POST.get('save'):
            room.name = request.POST.get('name')
            room.available = request.POST.get('available')
            room.save()
        return redirect("home")



class ViewRoom(View):
    def get(self, request, room_id):
        room = Room.objects.get(id=room_id)
        return render(request, "room_view.html", {"room": room})


class ListReservation(View):
    def get(self, request):
        reservations = Reservations.objects.all()
        ctx = {"reservs": []}
        for r in reservations:
            ctx["reservs"].append([r.id, r.room.name, r.reserved_from, r.reserved_until])
        return render(request, "reservation_list.html", ctx)


class AddReservation(View):
    def get(self, request):
        ctx = {'rooms': []}
        rooms = Room.objects.filter(available=True)
        for room in rooms:
            ctx['rooms'].append([room.id, room.name])
        return render(request, "reservation_add.html", ctx)

    def post(self, request):
        date_from = request.POST.get('from')
        date_until = request.POST.get('until')
        room_id = request.POST.get('room')
        room = Room.objects.get(id=room_id)
        res = Reservations.objects.create(reserved_from=date_from, reserved_until=date_until, room=room)
        return redirect('reservations_list')

