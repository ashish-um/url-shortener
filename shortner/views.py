from django.shortcuts import render, redirect
import uuid
from .models import Url
from django.http import HttpResponse


def index(request):
    if request.method == 'POST':
        url = request.POST['link']
        if Url.objects.filter(link=url).exists():
            print("URL Exists")
            request.session['message'] = Url.objects.get(link=url).link + "  Short Hand:localhost:8000/" + Url.objects.get(link=url).uuid
            return redirect('index')
        else:
            print("URL DOES NOT EXIST" + url)
            uid = str(uuid.uuid4())[:5]
            new_url = Url(link=url, uuid=uid)
            new_url.save()
            return render(request, 'index.html', {'uid': uid})


    return render(request, 'index.html')

def go(request, pk):
    url_details = Url.objects.get(uuid=pk)
    return redirect( url_details.link)