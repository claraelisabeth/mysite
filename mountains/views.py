from django.shortcuts import render
from mountains.models import Mountain

def mountain_index(request):
    mountains = Mountain.objects.all()
    context = {
        "mountains" : mountains
    }
    return render(request, "mountains/mountain_index.html", context)

def mountain_detail(request, pk):
    mountain = Mountain.objects.get(pk=pk)
    context = {
        "mountain": mountain
    }
    return render(request, "mountains/mountain_detail.html", context)