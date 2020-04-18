from django.shortcuts import render,redirect
from .models import Employee
from .forms import EmployeeForm


def index(request):
    emp = Employee.objects.all()
    return render(request,'employee/index.html',{'emp':emp})

def delete(request,emp_id):
    emp_to_delete = Employee.objects.get(pk=emp_id)
    emp_to_delete.delete()
    return redirect('index')

def add(request):
    if request.method == "POST":
        form = EmployeeForm(request.POST or None)
        if form.is_valid():
            form.save()
            return redirect('index')
        else:
            return redirect('add')    
    else:
        return render(request,'employee/add.html',{})

def edit(request,emp_id):
    if request.method == "POST":
        emp_to_edit = Employee.objects.get(pk=emp_id)
        form = EmployeeForm(request.POST or None,instance=emp_to_edit)
        if form.is_valid():
            form.save()
            return redirect('index')
        else:
            return redirect('edit')    
    else:
        emp_to_edit = Employee.objects.get(pk=emp_id)
        return render(request,'employee/edit.html',{'emp_edit':emp_to_edit})
   
    
       