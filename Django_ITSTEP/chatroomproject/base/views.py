from django.shortcuts import render

rooms = [
    {'id': 1, "name": "Python SOLID Principles" },
    {'id': 2, "name": "Python Formatting"},
    {'id': 3, "name": "Python OOP"}
]


def home(request):
    return render(request,'base/home.html', {"rooms": rooms})

def room(request):
    return render(request,'base/room.html')