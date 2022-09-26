from django.shortcuts import render, get_object_or_404
from .models import Post
from .forms import Form


# Create your views here.
def index(request):
    posts = Post.objects.all()
    return render(request, 'copa/index.html',
                  {'posts': posts})


def games(request):
    posts = Post.objects.all().filter(category='3')
    return render(request, 'copa/index.html',
                  {'posts': posts})


def controversies(request):
    posts = Post.objects.all().filter(category='1')
    return render(request, 'copa/index.html',
                  {'posts': posts})


def players(request):
    posts = Post.objects.all().filter(category='2')
    return render(request, 'copa/index.html',
                  {'posts': posts})


def show_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    posts = Post.objects.all()
    return render(request, 'copa/show_post.html', {
        'post': post,
        'posts': posts
    }
)


def make_post(request):
    if request.method == 'GET':
        form = Form()
        return render(request, 'copa/make_post.html', {'form': form})
    else:
        form = Form(request.POST)
        if form.is_valid():
            cadastro = form.save()
            form = Form()
            return index(request)
        else:
            return render(request, "copa/make_post.html",
                          {'form': form})

def search_value(request):

    return render(request, 'copa/index.html',
                  {'posts': posts})