from django.shortcuts import render
from .forms import RegisterForm
from django.views import View

# Create your views here.

class RegisterView(View):
    def get(self,request):
        form = RegisterForm()
        context = {
            'form':form
        }
        return render(request,'registration/register.html',context)
    
