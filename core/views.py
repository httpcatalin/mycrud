from django.shortcuts import render
from item.models import Category, Item

def index(request):
    items = Item.objects.filter(is_sold=False)
    categories = Category.objects.all()
    return render(request,'core/index.html',{'items':items, 'categories':categories})

def contact(request):
    return render(request, 'core/contact.html')