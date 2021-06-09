
from django.shortcuts import redirect, render
from .models import Dragon, Rider
from django.contrib import messages

# Create your views here.
#localhost:8000
def index(request):
    return render(request,"index.html")

#localhost:8000/dragons
def show_dragons(request):
    context = {
        "all_dragons": Dragon.objects.all()
    }
    return render(request,"show_dragons.html", context)

#localhost:8000/dragons/new
def new_dragons(request):
    context = {
        "all_riders":Rider.objects.all()
    }
    return render(request,"new_dragons.html", context)

#localhost:8000/dragons/create
def create_dragons(request):
    if request.method == 'POST': 
        

        errors = Dragon.objects.dragon_creator_validator(request.POST)
        # check if the errors dictionary has anything in it
        if len(errors) > 0:
            # if the errors dictionary contains anything, loop through each key-value pair and make a flash message
            for value in errors.values():
                messages.error(request, value)
            # redirect the user back to the form to fix the errors
            return redirect('/dragons/new')

        else:
            # if the errors object is empty, that means there were no errors!
            # retrieve the blog to be updated, make the changes, and save
            #create dragon
            Dragon.objects.create(name=request.POST['name'] , num_of_wings=request.POST['num_of_wings'] , has_magic=request.POST['has_magic'], my_rider = Rider.objects.get(id=request.POST['rider_id']))
            print("I am creating a Dragon!")
            return redirect("/dragons")
    return redirect('/dragons/new')

#lovalhost:8000/dragons/like
def like_dragons(request, dragon_id):
    #need a rider
    rider = Rider.objects.get(id=1)
    #need a dragon
    dragon = Dragon.objects.get(id=dragon_id)
    #get dragons list of riders who like
    liking_riders = dragon.riders_that_like_me
    #add rider to list of riders
    liking_riders.add(rider)
    return redirect("/dragons")

def unlike_dragons(request, dragon_id):
    #need a rider
    rider = Rider.objects.get(id=1)
    #need a dragon
    dragon = Dragon.objects.get(id=dragon_id)
    #get dragons list of riders who like
    liking_riders = dragon.riders_that_like_me
    #add rider to list of riders
    liking_riders.remove(rider)
    return redirect("/dragons")

#localhost:8000/dragons/{id}/edit
def edit_dragons(request, dragon_id):
    context = {
        "dragon_id":dragon_id,
    }
    return render(request,"edit_dragons.html", context)

#localhost:8000/dragons/{id}/update
def update_dragons(request, dragon_id):
    if request.method == 'POST': 
        
        errors = Dragon.objects.dragon_creator_validator(request.POST)
        # check if the errors dictionary has anything in it
        if len(errors) > 0:
            # if the errors dictionary contains anything, loop through each key-value pair and make a flash message
            for value in errors.values():
                messages.error(request, value)
            # redirect the user back to the form to fix the errors
            return redirect('/dragons/new')

        else:
            # if the errors object is empty, that means there were no errors!
            # retrieve the blog to be updated, make the changes, and save
            #create dragon
            thisDragon = Dragon.objects.get(id=dragon_id)
            thisDragon.name=request.POST['name']
            thisDragon.num_of_wings=request.POST['num_of_wings']
            thisDragon.has_magic=request.POST['has_magic']
            thisDragon.save()
            return redirect(f"/dragons/{dragon_id}")
    return redirect(f'/dragons/{dragon_id}/edit')

def destroy(request, dragon_id):
    dragon_to_delete = Dragon.objects.get(id=dragon_id)
    dragon_to_delete.delete()
    return redirect("/dragons")