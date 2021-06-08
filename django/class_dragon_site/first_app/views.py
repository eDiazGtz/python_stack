from django.shortcuts import redirect, render
from .models import Dragon, Rider

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