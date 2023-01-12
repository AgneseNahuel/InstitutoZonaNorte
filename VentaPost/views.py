from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from django.contrib.auth.decorators import login_required
from .forms import *
from django.contrib import messages


@login_required
def feed(request):
    posts = Post.objects.all()

    context = {'posts': posts}
    return render(request, 'feed.html', context)

@login_required
def profile(request):
    return render(request, 'profile.html')

@login_required
def post(request):
    current_user = get_object_or_404(User, pk=request.user.pk)
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = current_user
            post.save()
            messages.success(request, 'Post Creado')
            return redirect('feed')
    else:
        form = PostForm()
    return render(request, 'post.html', {'form': form})