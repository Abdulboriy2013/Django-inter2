from django.shortcuts import redirect, render
from django.db import IntegrityError
from maqola.models import Maqola, Comment, Like

# Create your views here.

def index(request):
    maqolalar = Maqola.objects.all().order_by('created_at')
    return render(request, 'index.html', {'maqolalar': maqolalar})

def detail(request, id):
    maqola = Maqola.objects.get(id=id)

    maqola.views += 1

    maqola.save()

    comment = Comment.objects.filter(maqola=maqola, status=True)

    comments_count = Like.objects.filter(maqola=id).count()

    likes_count = Like.objects.filter(maqola=id).count()

    return render(request, 'detail.html', {'maqola': maqola, 'comments': comment, 'likes_count': likes_count, 'comments_count': comments_count})

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
    return render(request, 'about.html')

#* like_post
def like_post(request, id):
    maqola = Maqola.objects.get(id=id)
    user = request.user
    try:
        like = Like.objects.create(user=user, maqola=maqola)
        return redirect('detail', id)
    except IntegrityError:
        like = Like.objects.filter(maqola = id, user=user)
        like.delete()
        return redirect('detail', id)
        