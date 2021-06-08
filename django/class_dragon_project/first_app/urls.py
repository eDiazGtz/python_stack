from django.urls import path
from . import views

urlpatterns = [
    path('', views.index), #localhost8000/
    path('dragons', views.show_dragons), #localhost8000/dragons
    path('dragons/new', views.new_dragons), #localhost8000/dragons/new
    path('dragons/create', views.create_dragons), #localhost8000/dragons/create
    path('dragons/<int:dragon_id>/edit', views.edit_dragons), #localhost8000/dragons/<id>/edit
]

