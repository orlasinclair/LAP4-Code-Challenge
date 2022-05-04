from django.shortcuts import render, redirect

from .models import UrlData
from .form import UrlForm
import random, string

# Create your views here.

def home(request):
    if request.method  == 'POST':
        form = UrlForm(request.POST)
        if form.is_valid():
            short = ''.join(random.choice(string.ascii_letters) for num in range(10))
            short_url = f"www.lazyurl/{short}"
            long_url = form.cleaned_data['long_url']
            new_url = UrlData(long_url=long_url, short_url=short_url)
            new_url.save()
            data = {
                'form': form,
                'new_url': new_url,
                'long_url': long_url
            }
            return render(request, 'base.html', data)
    else:
        form = UrlForm()
    data = UrlData.objects.all()
    context = {
        'form': form
    }
    return render(request, 'base.html', context)
