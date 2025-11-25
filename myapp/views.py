from django.shortcuts import render , redirect , reverse
from django.contrib import messages
from django.views import View
from django.http import HttpResponseRedirect

from .forms import ContactUsForm


from .models import NewsDatabase

# Create your views here.



def index(request):
    news = NewsDatabase.objects.all()
    return  render(request , 'myapp/index.html' , context={'news':news} )




def index_dark(request):
    return render(request , 'myapp/index-dark.html' )



def intro(request):
    return render(request , 'myapp/intro.html' )





class ContactUsView(View):
    template_name = 'myapp/index.html'

    def get(self, request, *args, **kwargs):
        form = ContactUsForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = ContactUsForm(request.POST)
        if form.is_valid():
            form.save()
            # ارسال پیغام به URL به صورت query parameter
            return HttpResponseRedirect(reverse('index') + '?message=فرم+شما+با+موفقیت+ارسال+شد!')
        else:

             return HttpResponseRedirect(reverse('index') + '?message=خطا+در+ارسال+فرم')




