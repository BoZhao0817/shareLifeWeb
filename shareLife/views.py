from django.shortcuts import render,get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.urls import reverse, reverse_lazy
from django.utils import timezone
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView,DeleteView
from django.views import generic
from message.models import Message
from .forms import SubmitPostForm, SearchPostForm
from message.form import MessageForm
from .models import Post, User, PostDetail,Location
from django.views import View


def index(request):
    if request.user.is_authenticated:
        post_list = Post.objects.all().exclude(author=request.user).order_by('-created_time')
        user_posts = Post.objects.filter(author=request.user).order_by('-created_time')
    else:
        user_posts = []
        post_list = Post.objects.all().order_by('-created_time')


    searchForm = SearchPostForm
    return render(request, 'index.html', context={'post_list':post_list, 'user_list':user_posts, 'search_form':searchForm})

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


def detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    # detail = get_object_or_404(PostDetail, pk = pk)
    print(request)
    # post.body = markdown.markdown(post.body,
    #                               extensions=[
    #                                   'markdown.extensions.extra',
    #                                   'markdown.extensions.codehilite',
    #                                   'markdown.extensions.toc',
    #                               ])
    # 记得在顶部导入 CommentForm
    form = MessageForm()
    # 获取这篇 post 下的全部评论
    message_list = Message.objects.all().filter(postId =pk)

    # 将文章、表单、以及文章下的评论列表作为模板变量传给 detail.html 模板，以便渲染相应数据。
    context = {'post':post,'message_form': form,'message_list': message_list}
    return render(request, 'detail.html', context=context)

def search(request):
    #time location bedrooms, tag
    if request.method == 'GET':
        bedrooms = request.GET.get('bedroom')
        location =  request.GET.get('location') # return id
        startDate = request.GET.get('startDate')
        endDate = request.GET.get('endDate')

        error_msg = ''
        post_list1 = Post.objects.filter(bedrooms = bedrooms)
        post_list2 = Post.objects.filter(location= location)
        post_list3 = Post.objects.filter(startDate__lte= startDate)
        post_list4 = Post.objects.filter(endDate__gte= endDate)

        post_list12 = post_list1 & post_list2
        post_list13 = post_list1 & post_list3
        post_list14 = post_list1 & post_list4
        post_list23= post_list2 & post_list3
        post_list24 =post_list2 & post_list4
        post_list34 = post_list3 & post_list4

        post_listSum2  = (post_list12|post_list23|post_list14|
                          post_list23|post_list24|post_list34).distinct()

        post_list123 = post_list12 & post_list3
        post_list234 = post_list23 & post_list4
        post_list124 = post_list12 & post_list4
        post_list134 = post_list13 & post_list4

        post_listSum3  = (post_list123|post_list234|post_list134|
                          post_list124).distinct()

        post_listSum4 = post_list12 & post_list34

        return render(request, 'result.html', {'error_msg': error_msg, 'post_list2':post_listSum2,
                                               'post_list3':post_listSum3,'post_list4':post_listSum4})


