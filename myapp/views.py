from django.shortcuts import render , redirect , reverse
from django.contrib import messages
from django.views import View
from django.http import HttpResponseRedirect
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render



from .forms import ContactUsForm , SignUpForm


from .models import NewsDatabase

# Create your views here.


#My index Page
def index(request):
    news = NewsDatabase.objects.all()
    return  render(request , 'myapp/index.html' , context={'news':news} )







class ContactUsView(View):
    template_name = 'myapp/index.html'

    def get(self, request, *args, **kwargs):
        form = ContactUsForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = ContactUsForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('index') + '?message=فرم+شما+با+موفقیت+ارسال+شد!')
        else:

             return HttpResponseRedirect(reverse('index') + '?message=خطا در ارسال فرم یا داده هایی که وارد کردین اشتباه هست')


