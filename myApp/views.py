from django.shortcuts import render, redirect
from .models import Employee
from .forms import EmployeeForm

# Create your views here.
def index(request):
    emp = Employee.objects.all()

    context ={
        'emp':emp
    }
    return render(request, 'index.html', context)


def GetData(request):
    if request.method=="POST":
        form = EmployeeForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect('/')
            except:
                pass
    else:
        form=EmployeeForm()
    return render(request, 'getdata.html', {'form':form})


def DataEdit(request, id):
    emp = Employee.objects.get(eid=id)
    return render(request, 'edit.html', {'emp':emp})



def update(request, id):
    emp = Employee.objects.get(eid=id)
    form = EmployeeForm(request.POST, instance = emp)  
    if form.is_valid():  
        form.save()  
        return redirect("/index")  
    return render(request, 'edit.html', {'emp': emp})

