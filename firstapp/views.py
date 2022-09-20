from django.shortcuts import render,redirect

from firstapp.models import Check
from .forms import CreateCheckForm

# Create your views here.



def Check_table(request):
    checkes = Check.objects.all()

    context = {
        'checkes':checkes
    }
    return render(request,'firstapp/Check_table.html',context)

def main_page(request):


    form = CreateCheckForm()
    if request.method == "POST":
        form = CreateCheckForm(request.POST)
        if form.is_valid():
            form.save()

            return redirect("Check_t")
        else:
            form= CreateCheckForm()

    context={
        'form' : form
    }

    return render(request,'firstapp/index.html',context)


def check_u(request,pk):
    check=Check.objects.get(id=pk)
    form = CreateCheckForm(instance=check)
    if request.method == "POST":
        form = CreateCheckForm(request.POST , instance=check)
        if form.is_valid():
            form.save()
            return redirect('Check_t')

        else :
            form = CreateCheckForm(instance=check)

    
    context={
        'form' : form
    }

    return render(request,'firstapp/index.html',context)


def check_d(request,pk):
    check = Check.objects.get(id=pk)
    if request.method == "POST":

        check.delete()
        return redirect('Check_t')

    context={
        'check':check
    }

    return render(request,'firstapp/check_d.html',context)

    