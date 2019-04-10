from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from django.utils import timezone
from django.views.generic.edit import CreateView, UpdateView,DeleteView
from .models import Post,User
from .forms import SubmitPostForm

def index(request):


    if request.user.is_authenticated:
        post_list = Post.objects.all().exclude(author=request.user).order_by('-created_time')
        user_posts = Post.objects.filter(author=request.user).order_by('-created_time')
    else:
        user_posts = []
        post_list = Post.objects.all().order_by('-created_time')


    return render(request, 'index.html', context={'post_list':post_list, 'user_list':user_posts})


def form(request):
    if request.method == 'POST':  # 当提交表单时

        form = SubmitPostForm(request.POST)  # form 包含提交的数据
        #TODO: not authenticated error
        if not request.user.is_authenticated:
            pass
        else:
            if form.is_valid():  # 如果提交的数据合法
                name = form.cleaned_data['name']
                body = form.cleaned_data['body']
                location = form.cleaned_data['location']
                # created_time = models.DateTimeField()
                # modified_time = models.DateTimeField()
                p = Post(name=name, body=body,
                        created_time=timezone.now(), modified_time=timezone.now(), author=request.user)
                p.save()
                return HttpResponseRedirect(reverse('index'))

    else:  #first
        form = SubmitPostForm()
    return render(request, 'form.html', {'form': form})

class updatePost(UpdateView):
    model = Post
    fields = ["name", "body","location", "address", 'startDate', 'endDate']
    labels = {'body': "Introduction"}
    help_texts = {'body': 'Tell us about your place' }
    success_url = reverse_lazy('index')

class deletePost(DeleteView):
    model = Post
    success_url = reverse_lazy('index')

