from django.shortcuts import render, HttpResponse, redirect

# Create your views here.
def index(request):
    return HttpResponse("This is my response")

def show_dragons(request):
    return render(request, "index.html")
    # return HttpResponse("This is a list of all Dragons")

def edit_dragon(request, dragon_id):
    context = {
        "dragon_id":dragon_id,
    }
    return render(request, "edit_dragon.html", context)
    # return HttpResponse(f"Edit Dragon with id {dragon_id}")

def create_dragons(request):
    #this is where we create a dragon
    return redirect("/")

