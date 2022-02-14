from django.shortcuts import render
from core.models import Event
from django.contrib.auth.decorators import login_required

# Create your views here.

def login_user(request):
    return render(request, 'login.html')

@login_required(login_url='/login/')
def list_events(request):
    #user = request.user
    #event = Event.objects.filter(user=user)
    event = Event.objects.all()
    response = {'events': event}
    return render(request, 'calendar.html', response)
