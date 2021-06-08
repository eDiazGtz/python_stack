from django.shortcuts import render, redirect

# Create your views here.
#/
def index(request):
    return render(request, "index.html") 

#/dragons (Show Dragons Here)
def show_dragons(request):
    if 'd_name' in request.session:
        context = {
            "all_dragons": request.session['d_name']
        }
        return render(request, "show_dragons.html", context)
    return render(request, "show_dragons.html")

#/dragons/new (Submit FORM HERE)
def new_dragons(request):
    return render(request, "new_dragons.html")

#/dragons/create (Create Dragons Here)
def create_dragons(request):
    if request.method == "POST":
        print("Dragon Created!")
        request.session['d_name'] = request.POST['dragon_name']
        return redirect("/dragons")
    return redirect("/dragons/new")



#/dragons/<dragon_id>/edit
def edit_dragons(request, dragon_id):
    context = {
        "dragon_id":dragon_id,
        "dragon_colors":['black', 'red', 'blue', 'green', 'white']
    }
    return render(request, "edit_dragon.html", context)
    # return HttpResponse(f"Edit Dragon with id {dragon_id}")
