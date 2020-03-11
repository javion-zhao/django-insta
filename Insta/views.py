from annoying.decorators import ajax_request
from django.views.generic import TemplateView ,ListView, DetailView
from Insta.models import Post
from django.views.generic.edit import CreateView,DeleteView,UpdateView
from django.urls import reverse_lazy

from Insta.forms import CostomUserCreationForm
from Insta.models import Like, InstaUser,Post,UserConnection,Comment
from django.contrib.auth.mixins import LoginRequiredMixin


class HelloWorld(TemplateView):
    template_name = 'test.html'

class PostListView(ListView):
    model = Post
    template_name = "home.html"

class PostDetailView(DetailView):
    model = Post
    template_name = "post_detail.html"

class PostCreatView( LoginRequiredMixin , CreateView):
    model = Post
    template_name = "post_creat.html"
    fields = '__all__'
    login_url = 'login'

class UserDetailView(LoginRequiredMixin,DetailView):
    model = InstaUser
    template_name = "user_detail.html"
    login_url = 'login'

class PostUpdateView(UpdateView):
    model = Post
    template_name = "post_update.html"
    fields = ['title']

class PostDeleteView( DeleteView ):
    model = Post
    template_name = "post_delete.html"
    success_url = reverse_lazy("index");

class SignUp (CreateView):
    form_class = CostomUserCreationForm
    template_name = "signup.html"
    success_url = reverse_lazy("login");


class EditProfile(LoginRequiredMixin,UpdateView):
    model=InstaUser
    template_name = "edit_profile.html"
    fields = ['profile_pic','username']
    login_url='login'

@ajax_request
def addLike(request):
    post_pk = request.POST.get('post_pk')
    post = Post.objects.get(pk=post_pk)
    try:
        like = Like(post=post, user=request.user)
        like.save()
        result = 1
    except Exception as e:
        like = Like.objects.get(post=post, user=request.user)
        like.delete()
        result = 0

    return {
        'result': result,
        'post_pk': post_pk
    }

@ajax_request
def addComment(request):
    comment_text = request.POST.get('comment_text')
    post_pk = request.POST.get('post_pk')
    post = Post.objects.get(pk=post_pk)
    commenter_info = {}
    try:
        comment = Comment(comment=comment_text, user=request.user, post=post)
        comment.save()

        username = request.user.username

        commenter_info = {
            'username': username,
            'comment_text': comment_text
        }

        result = 1
    except Exception as e:
        print(e)
        result = 0

    return {
        'result': result,
        'post_pk': post_pk,
        'commenter_info': commenter_info
    }

@ajax_request
def toggleFollow(request):
    current_user = InstaUser.objects.get(pk=request.user.pk)
    follow_user_pk = request.POST.get('follow_user_pk')
    follow_user = InstaUser.objects.get(pk=follow_user_pk)

    try:
        if current_user != follow_user:
            if request.POST.get('type') == 'follow':
                connection = UserConnection(creator=current_user, following=follow_user)
                connection.save()
            elif request.POST.get('type') == 'unfollow':
                UserConnection.objects.filter(creator=current_user, following=follow_user).delete()
            result = 1
        else:
            result = 0
    except Exception as e:
        print(e)
        result = 0

    return {
        'result': result,
        'type': request.POST.get('type'),
        'follow_user_pk': follow_user_pk
    }
