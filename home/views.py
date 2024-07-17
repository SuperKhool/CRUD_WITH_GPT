from django.shortcuts import redirect, render ,HttpResponse , get_object_or_404
from .models import Employ
from .forms import Empolyeform

# Create your views here.

def home(requset):
    employe = Employ.objects.all()
    context = {
        'employe':employe,
    }
    return render(requset,"home.html",context)




def add_employe(request):
    if request.method == 'POST':
         
        form = Empolyeform(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    form = Empolyeform()
    context = {
        'form':form
        }
    return render(request, 'add_employe.html', context)





def edit_employe(request, id):
    employe = get_object_or_404(Employ, id=id)
    
    if request.method == 'POST':
        form = Empolyeform(request.POST, instance=employe)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = Empolyeform(instance=employe)
    
    context = {
        "form": form,
        "employe": employe,
    }
    
    return render(request, 'card.html', context)


def  delete_employe(requset,id):
    delete_employe = get_object_or_404(Employ,id=id)
    delete_employe.delete()
    
    return redirect('home')