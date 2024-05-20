from django.shortcuts import render,redirect
from .models import Task
from .forms import Todo
def index(req):
    t=Task.objects.all()
    if req.method=='POST':
        name=req.POST.get('name')
        pr=req.POST.get('priority')
        dt=req.POST.get('date','')
        obj=Task(name=name,priority=pr,date=dt)
        obj.save()
        return redirect('/')
    return render(req,'myapp/index.html',{'task':t})
def delete(req,id):
    t=Task.objects.get(id=id)
    if req.method=="POST":
        t.delete()
        return redirect('/')
    return render(req,'myapp/delete.html',{'task':t})

def update(req,id):
    t=Task.objects.get(id=id)
    f=Todo(req.POST or None,instance=t)
    if f.is_valid():
        f.save()
        return redirect('/')
    return render(req,'myapp/update.html',{'form':f,'task':t})
# Create your views here.
