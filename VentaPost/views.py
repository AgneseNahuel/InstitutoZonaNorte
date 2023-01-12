from django.shortcuts import render
from .models import *
from django.contrib.auth.decorators import login_required

@login_required
def feed(request):
    posts = Post.objects.all()

    context = {'posts': posts}
    return render(request, 'feed.html', context)

@login_required
def profile(request):
    return render(request, 'profile.html')
