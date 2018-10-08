from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Homework

# Create your views here.

def index(request):
    nodes_list = Homework.objects.all()

    template = loader.get_template('homeworks/index.html')
    context = {
        'homeworks': nodes_list,
    }

    return HttpResponse(template.render(context, request))

def show(request):
    return HttpResponse("TODO:")