from django.shortcuts import render, redirect

from .models import UrlData
from .form import UrlForm
import random, string

# Create your views here.

def home(request):
    if request.method  == 'POST':
        form = UrlForm(request.POST)
        if form.is_valid():
            short_url = ''.join(random.choice(string.ascii_letters) for num in range(10))
            # short_url = f"http://localhost:8000/{short}"
            long_url = form.cleaned_data['long_url']
            new_url = UrlData(long_url=long_url, short_url=short_url)
            new_url.save()
            data = {
                'form': form,
                'new_url': new_url,
                'long_url': long_url
            }
            test = UrlData.objects.get(short_url=short_url)
            print(test.long_url)
            return render(request, 'base.html', data)
    else:
        form = UrlForm()
    data = UrlData.objects.all()

    context = {
        'form': form
    }
    return render(request, 'base.html', context)


def RedirectedUrl(request, short):
    data = UrlData.objects.get(short_url=short)
    return redirect(data.long_url)
