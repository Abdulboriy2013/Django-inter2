from django.shortcuts import render
from maqola.models import Maqola

# Create your views here.

def index(request):
    maqolalar = Maqola.objects.all().order_by('created_at')
    return render(request, 'index.html', {'maqolalar': maqolalar})

def detail(request, id):
    maqola = Maqola.objects.get(id=id)
    return render(request, 'detail.html', {'maqola': maqola})