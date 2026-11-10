from django.urls import path
from . import views

# Url para el dashboard
urlpatterns = [
    path("", views.index, name="dashboard")

]
