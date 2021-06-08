from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('dragons', views.show_dragons),
    path('dragons/new', views.new_dragons),
    path('dragons/create', views.create_dragons),
    path('dragons/<int:dragon_id>/edit', views.edit_dragons),
    path('dragons/<int:dragon_id>/like', views.like_dragons),
    path('dragons/<int:dragon_id>/unlike', views.unlike_dragons),
]
