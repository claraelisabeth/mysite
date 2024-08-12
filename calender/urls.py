
from django.urls import path
from calender import views

urlpatterns = [
    path("", views.schedule_view, name='schedule'),
]