from django.shortcuts import render
from django.http import HttpResponse
from .import models


def index(request):
    pys=models.art.objects.all()
    return render(request,'order_list.html',{'pys':pys})