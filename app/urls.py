from django.urls import path
from . import views

urlpatterns = [
    path("", views.upload, name="upload"),
    path('my-django-view-url/', views.my_ajax_view, name='my_ajax_view'),
]