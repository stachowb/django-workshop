from django.shortcuts import render, redirect
from django.http import Http404, HttpResponse
from django.views import View
from django.views.generic.edit import DeleteView
from workshop.models import Room
from django.contrib import messages


class FrontPage(View):

    URL = "http://127.0.0.1:8000/"
    template = 'front_page1.html'

    def get(self, request):
        rooms = Room.objects.all()
        ctx = {'rooms': []}
        for room in rooms:
            ctx['rooms'].append([room.id, room.name, room.available])
        return render(request, self.template, ctx)

    def post(self, request):
        response = HttpResponse()

        if add := request.POST.get('add'):
            name = request.POST.get("r_name")
            try:
                room = Room(name=name)
                room.save()
                messages.info(request, "Room added successfully!")
            except:
                pass

            return redirect(self)

        if edit := request.POST.get('edit'):
            pass

        if view := request.POST.get('view'):
            pass

    def get_absolute_url(self):
        return self.URL


class DeleteRoom(View):

    def get(self, request, room_id):
        return render(request, "delete.html")

    def post(self, request, room_id):
        room = Room.objects.get(id=room_id)
        room.delete()
        return redirect("home")
