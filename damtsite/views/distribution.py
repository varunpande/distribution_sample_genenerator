from django.shortcuts import render
from django.template import loader

def dist(request,distribution_type):
    return render(request,'input_param.html',{'dist_type' : distribution_type})
