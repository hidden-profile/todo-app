#django provides buitin class based views called generic views 
#ex ListView,Detailview,Createview,Updateview,Deleteview
from django.shortcuts import render,redirect
from .models import Task
from .forms import Todo
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView,DeleteView
from django.urls import reverse_lazy

class TListview(ListView):
    model=Task
    template_name='myapp/index.html'
    #compulsary same var names
    #context obj
    context_object_name='task'
    #associate with url
    #in urls.py
    # path('view/',classbasedgenericview.TListView,name='view')
class TDetailview(DetailView):
    model=Task
    template_name='myapp/detail.html'
    context_object_name='task'
    #connect with url
    # path('detail/<int:pk>/',views.TDetailview.as_view(),name='detail') pk-->primarykey
class TUpdate(UpdateView):
    model=Task
    template_name='myapp/update1.html'
    fields=('name','priority','date')
    context_object_name='task'

    def get_success_url(self) -> str:
        return reverse_lazy('detail',kwargs={'pk':self.object.id})
    #path('update/<int:pk>/'views.TUpdate.as_view(),name='update')
class TDelete(DeleteView):
    model=Task
    template_name='myapp/delete.html'
    success_url=reverse_lazy('view')
    #path('de/<int:pk>/'views.TDelete.as_view(),name='del')