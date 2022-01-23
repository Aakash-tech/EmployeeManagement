from ast import Param
from os import name
from django.shortcuts import render
from .models import Employee,Department,Role
from django.http import HttpResponse
from django.db.models import Q
# Create your views here.
def index(request):
    return render(request,'index.html')

def all_emp(request):
    data = Employee.objects.all()
    param={"emp":data}
    return render(request,'all_emp.html',param)

def add_emp(request):
    if request.method=='POST':
        first_name=request.POST.get('first_name','')
        last_name=request.POST.get('last_name','')
        dept=request.POST.get('dept','')
        salary=int(request.POST.get('salary',''))
        bonus=int(request.POST.get('bonus',''))
        role=request.POST.get('role','')
        phone=int(request.POST.get('phone',''))

        employee=Employee(first_name=first_name,last_name=last_name,dept_id=dept,salary=salary,bonus=bonus,role_id=role,phone=phone)
        employee.save()
    return render(request,'add_emp.html')

def del_emp(request,id=0):
    if id:
        data2=Employee.objects.get(id=id)
        data2.delete()
        return HttpResponse("removed Successfully")
    data = Employee.objects.all()
    param={"emp":data}
    return render(request,'del_emp.html',param)


def filter_emp(request):
    if request.method=="POST":
        name=request.POST.get('name','')
        dept=request.POST.get('dept','')
        role=request.POST.get('role','')
        emp=Employee.objects.all()
        if name:
            emp = emp.filter(Q(first_name__icontains=name) | Q(last_name__icontains=name))
        if dept:
            emp = emp.filter(dept__name=dept)
        if role:
            emp = emp.filter(role__name=role)
        param={"emp":emp}
        return render(request,'all_emp.html',param)

    return render(request,'filter_emp.html')