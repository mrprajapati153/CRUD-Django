from django.shortcuts import render, HttpResponseRedirect
from .forms import StudentRegistration
from .models import user

# add the data and show the data


def add_show(requset):
    if requset.method == 'POST':
        fm = StudentRegistration(requset.POST)
        if fm.is_valid():
            nm = fm.cleaned_data['name']
            em = fm.cleaned_data['email']
            pw = fm.cleaned_data['password']
            reg = user(name=nm, email=em, password=pw)
            reg.save()
            fm = StudentRegistration()
    else:
        fm = StudentRegistration()
    stud = user.objects.all()

    return render(requset, 'enroll/addandshow.html', {'form': fm, 'stu': stud})

def delete_data(request,id):
    if request.method == 'POST':
     pi = user.objects.get(pk=id)
     pi.delete()
     return HttpResponseRedirect('/')     
 
def update_data(request,id):
    if request.method=='POST':
        pi=user.objects.get(pk=id)
        fm=StudentRegistration(request.POST,instance=pi)
        if fm.is_valid():
           fm.save()
    else:
        pi=user.objects.get(pk=id)
        fm=StudentRegistration(instance=pi)
    
    return render(request,'enroll/updatestudent.html',{'form':fm})
