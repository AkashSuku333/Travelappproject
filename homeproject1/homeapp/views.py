from django.http import HttpResponse
from django.shortcuts import render
from . models import place
from . models import team

# Create your views here.
def homepage(request):

    result1 = place.objects.all()
    result2 = team.objects.all()



    demo = {'result1':result1,'result2':result2}

    return render(request,"index.html",demo)






# def home(request):
#     book = crew.objects.all()
#     return render(request,"index.html",{'res':book})
# def about(request):
#     return render(request,"about.html")
# def contact(request):
#     return render(request,"contact.html")
# def details(request):
#     return HttpResponse("details page")
# def thanks(request):
#     return HttpResponse("thankyou all")