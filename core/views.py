from django.shortcuts import render
from core.models import Event


# Create your views here.

def list_events(request):
    #user = request.user
    #event = Event.objects.filter(user=user)
    event = Event.objects.all()
    response = {'events': event}
    return render(request, 'calendar.html', response)
