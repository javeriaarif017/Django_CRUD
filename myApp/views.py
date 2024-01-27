from django.shortcuts import render, redirect, get_list_or_404
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



def update(request, pk):
    emp = Employee.objects.get(id=pk)
    form = EmployeeForm(request.POST, instance = emp)  
    if form.is_valid():  
        form.save()  
        return redirect("/")  
    return render(request, 'edit.html', {'emp': emp})

def delete(request, pk):  
    employee = Employee.objects.get(id=pk)  
    employee.delete()  
    return redirect("/")  

