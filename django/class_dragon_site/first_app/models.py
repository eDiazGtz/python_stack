from django.db import models

# Create your models here.

class DragonManager(models.Manager):
    def dragon_creator_validator(self, postData):
        errors = {}
        if len(postData['name']) < 2:
            errors['name'] = "Hey, name has to be at least 2 characters"
        if len(postData['num_of_wings']) == 0:
            errors['num_of_wings'] = "Hey, Number of Wings has to be at least 1 number"
        return errors

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
    objects = DragonManager()
    