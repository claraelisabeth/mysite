from django.db import models

class Subject(models.Model):
    name = models.CharField(max_length=50, primary_key=True)
    number = models.CharField(max_length=10)
    ects = models.IntegerField()
    sub_type = models.CharField(max_length=2, choices={"VO":"VO","VU":"VU","UE":"UE","PR":"PR","SE":"SE"})
    professor = models.CharField(max_length=50)
    comment = models.CharField(max_length=100)
    done = models.BooleanField(blank=True)
    hours = models.IntegerField()
    timeframe = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.number} {self.sub_type} {self.name}"
                                
class Module(models.Model):
    name = models.CharField(max_length=50, primary_key=True)
    description = models.CharField(max_length=200)
    
class SubjectModuleRel(models.Model):
    subject = models.ForeignKey(Subject,  on_delete=models.CASCADE)
    module = models.ForeignKey(Module)
    core_ex = models.CharField(max_length=1, choices={"C":"Core","E":"Extension"})

class TopicOfInterest(models.Model):
    topic=models.CharField(max_length=50)
    comment=models.CharField(max_length=300)