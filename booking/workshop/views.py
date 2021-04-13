from django.shortcuts import render, redirect
from django.http import Http404, HttpResponse
from django.views import View
from workshop.models import Room
from django.contrib import messages

class FrontPage(View):
    URL = "http://127.0.0.1:8000/"

    def get(self, request):
        rooms = Room.objects.all()
        ctx = {'rooms': []}
        for room in rooms:
            ctx['rooms'].append([room.id, room.name, room.available])
        return render(request, 'front_page1.html', ctx)

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

        if delete_id := request.POST.get('delete'):
            room = Room.objects.get(id=delete_id)
            room.delete()
            response.write("Usunieto z bazy")

            return response

    def get_absolute_url(self):
        return self.URL

