from django.urls import path
from mountains import views

urlpatterns = [
    path("", views.mountain_index, name="mountain_index"),
    path("<int:pk>/", views.mountain_detail, name="mountain_detail"),
]