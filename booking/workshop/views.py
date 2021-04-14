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

        if delete := request.POST.get('delete'):
            return redirect(DeleteRoom)

        if edit := request.POST.get('edit'):
            pass

        if view := request.POST.get('view'):
            pass

    def get_absolute_url(self):
        return self.URL


class DeleteRoom(DeleteView):
    model = Room
    template_name = "delete.html"
    success_url = ""

    def delete(self, request, *args, **kwargs):
        room = Room.objects.get(id=1)
        room.delete()
        return super(DeleteRoom, self).delete(request, *args, **kwargs)

    def get_absolute_url(self):
        return self.success_url