from django.urls  import path
from django.http import HttpResponse

def home(request):
    return HttpResponse("<h1>Home Page</h1>")

def room(request):
    return HttpResponse('<h1>Rooms Page</h1>')


urlpatterns = [
    path('', home),
    path('room/', room)
]
