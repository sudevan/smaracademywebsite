from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")
# Create your views here.
class Homepageview(View):
    template_name = 'index.html'
    def get(self,request,*args,**kwargs):
        context ={}
        #return HttpResponse("Hello, world. You're at the polls index.")
        return render(request,self.template_name,context)