from django.shortcuts import render
from maqola.models import Maqola, Comment

# Create your views here.

def index(request):
    maqolalar = Maqola.objects.all().order_by('created_at')
    return render(request, 'index.html', {'maqolalar': maqolalar})

def detail(request, id):
    maqola = Maqola.objects.get(id=id)
    comment = Comment.objects.filter(maqola=maqola, status=True)
    return render(request, 'detail.html', {'maqola': maqola, 'comments': comment})