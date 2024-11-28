from django.shortcuts import render
from django.http import HttpResponse
from .models import Member
from django.template import loader

import datetime
# Create your views here.
def Home(request):
    # return render(request, 'index.html')
    mylogo = 'Early Code'
    template = loader.get_template('index.html')
    context ={
        "mylogo" : mylogo,
        "mydate" :datetime.datetime.now(

            
        )
    }
    return HttpResponse(template.render(context, request))


def about(request):
    return render(request, 'about.html')

def members(request):
    mymembers= Member.objects.all().values()
    template= loader.get_template("all_members.html")
    context = {
        "mymembers":mymembers
    }
    return HttpResponse(template.render(context, request))

def details(request,  id):
    mymember=Member.objects.get(id=id)
    template= loader.get_template("details.html")
    context={
        'mymember':mymember
    }
    return HttpResponse(template.render(context, request))



