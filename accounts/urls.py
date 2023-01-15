from django.urls import path
from . import views

urlpatterns = [path("analyse", views.verify, name="analyse")]    
