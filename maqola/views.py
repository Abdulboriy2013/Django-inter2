from django.shortcuts import redirect, render
from maqola.models import Maqola, Comment

# Create your views here.

def index(request):
    maqolalar = Maqola.objects.all().order_by('created_at')
    return render(request, 'index.html', {'maqolalar': maqolalar})

def detail(request, id):
    maqola = Maqola.objects.get(id=id)
    comment = Comment.objects.filter(maqola=maqola, status=True)
    return render(request, 'detail.html', {'maqola': maqola, 'comments': comment})

#* Comment
def comment(request):
    if request.method == 'POST':
        user = request.user

        body = request.POST.get('comment')

        maqolaId = request.POST.get('maqolaId')

        maqola = Maqola.objects.get(id=maqolaId)

        new_comment = Comment.objects.create(user=user, comment=body, maqola=maqola)

        return redirect('detail', maqola.id)
    
#! About
def about(request):
    return redirect(request, 'about.html')