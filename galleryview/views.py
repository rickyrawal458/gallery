from django.shortcuts import render
from  django.views.generic import CreateView,DetailView
from .models import List
from django.core.paginator import Paginator
from django.shortcuts import get_object_or_404

def list(request):
    list=List.objects.all()
    paginator= Paginator(list,8)
    page=request.GET.get('page')
    list=paginator.get_page(page)
    return render(request,'list.html',{'list':list})

class Addpost(CreateView):
    model= List
    template_name = 'addpost.html'
    fields = '__all__'

class ListDeatailView(DetailView):
    model=List
    template_name = 'detail.html'



