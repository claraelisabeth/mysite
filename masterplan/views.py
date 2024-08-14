from django.shortcuts import render
from masterplan.models import Subject, Module, SubjectModuleRel, TopicOfInterest

def master_index(request):
    modules = Module.objects.all()
    subjects = Subject.objects.all()
    sm_rel = SubjectModuleRel.objects.all()
    topic = TopicOfInterest.objects.all()

    context = {
        "modules" : modules,
        "subjects" : subjects,
        "sm_rel" : sm_rel,
        "topic" : topic
    }
    return render(request, "masterplan/master_index.html", context)
