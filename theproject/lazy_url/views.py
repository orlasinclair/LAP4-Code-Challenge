from django.shortcuts import render, redirect

from theproject.lazy_url.models import UrlData
from .form import UrlForm
import random, string

# Create your views here.

def home(request):
    if request.method  == 'POST':
        form = UrlForm(request.POST)
        if form.is_valid():
            short_url = ''.join(random.choice(string.ascii_letters) for num in range(10))
            url = form.cleaned_data['url']
            new_url = UrlData(url=url, short_url=short_url)
            new_url.save()
            return redirect('lazy-url-home')
    else:
        form = UrlForm()
        data = {'form': form}

    return render(request, 'base.html', data)
