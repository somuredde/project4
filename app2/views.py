from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def sample3(request):
    return HttpResponse('this is sample3')
def sample4(request):
    return HttpResponse('this is sample4')