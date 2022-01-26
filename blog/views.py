from django.shortcuts import render,redirect
from .models import Post, Category, Comment
from .forms import CommentForm

# Create your views here.

def index(request):
    posts = Post.objects.all().order_by('-create_on')
    context = { "posts": posts }
    return render(request, 'blog_index.html', context)

def category(request, category):
    posts = Post.objects.filter(
        categories__name__contains=category
    ).order_by('-create_on')
    context = {
        'category': category,
        'posts': posts
    }

    return render(request, 'blog_category.html', context)


def blog_detail(request, pk):
    post = Post.objects.get(pk=pk)

    form = CommentForm()

    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = Comment(
                author=form.cleaned_data['author'],
                body=form.cleaned_data['body'],
                post=post
            )
            comment.save()
            return redirect('blog_index')
        else:
            form = CommentForm()
            
    comments = Comment.objects.filter(post=post)
    context = {
        'post': post,
        'comments': comments,
        "form": form
    }
    return render(request, 'blog_detail.html', context)