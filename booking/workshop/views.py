from django.shortcuts import render, redirect
from django.http import Http404, HttpResponse
from django.views import View
from django.views.generic.edit import DeleteView
from workshop.models import Room, Reservations
from django.contrib import messages


class FrontPage(View):

    URL = "http://127.0.0.1:8000/"

    def get(self, request):
        rooms = Room.objects.all()
        ctx = {'rooms': []}
        for room in rooms:
            ctx['rooms'].append([room.id, room.name, room.available])
        return render(request, "room_list.html", ctx)

    def post(self, request):
        if request.POST.get('add'):
            name = request.POST.get("r_name")
            try:
                room = Room(name=name)
                room.save()
                messages.info(request, "Room added successfully!")
            except:
                pass

            return redirect(self)

    def get_absolute_url(self):
        return self.URL


class DeleteRoom(View):

    def get(self, request, room_id):
        return render(request, "room_delete.html")

    def post(self, request, room_id):
        if request.POST.get('confirm'):
            room = Room.objects.get(id=room_id)
            room.delete()
            return redirect("home")
        if request.POST.get("deny"):
            return redirect("home")


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
        if request.POST.get('back'):
            return redirect("home")


class ViewRoom(View):
    def get(self, request, room_id):
        room = Room.objects.get(id=room_id)
        return render(request, "room_view.html", {"room": room})


class ManageReservations(View):
    def get(self, request):
        reservations= Reservations.objects.all()
        ctx = {"resevs": []}
        for r in reservations:
            ctx["resevs"].append([r.id, r.room.name, r.reserved_from, r.reserved_until])
        return render(request, "reservations.html", ctx)

    def post(self, request):
        pass