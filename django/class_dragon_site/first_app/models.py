from django.db import models

# Create your models here.
class Rider(models.Model):
    name = models.CharField(max_length=17)
    guild = models.CharField(max_length=15)
    is_trained = models.BooleanField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    #my_dragons
    #dragons_liked
class Dragon(models.Model):
    #id
    name = models.CharField(max_length = 17)
    num_of_wings = models.IntegerField()
    has_magic = models.BooleanField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    my_rider = models.ForeignKey(Rider, related_name="my_dragons", on_delete = models.CASCADE)
    riders_that_like_me = models.ManyToManyField(Rider, related_name="dragons_liked")
    #objects