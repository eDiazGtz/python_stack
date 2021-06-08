from django.urls import path
from . import views

urlpatterns = [
    path('', views.index), #/java
    path('dragons', views.show_dragons), #localhost8000/ + dragons
    path('dragons/create', views.create_dragons), #localhost8000/ + dragons
    path('dragons/<int:dragon_id>/edit', views.edit_dragon),
]