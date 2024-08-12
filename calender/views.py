from django.shortcuts import render
from django.http import HttpResponse
from calender.models import Subject
from calender.models import Freetime
import datetime

### functions or classes are mapped to urls

def schedule_view(request):
    subjects = Subject.objects.all()
    freetimes = Freetime.objects.all()

    hours = [datetime.time(i,0,0) for i in range(7,22)]
    days = ['Monday', 'Tuesday','Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    context = {
        "subjects": subjects,
        "freetimes": freetimes,
        "hours": hours,
        "days": days,
    }

    return render(request, "calender/table.html", context)


def detail_view(request, pk):
    subject = Subject.objects.get(pk=pk)
    freetime = Freetime.objects.get(pk=pk)
    context = {
        "subject": subject,
        "freetime": freetime,
    }
    return render(request, "calender/detail.html", context)