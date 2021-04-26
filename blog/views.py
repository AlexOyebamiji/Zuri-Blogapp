from django.shortcuts import render
from .models import Post, Comment
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, FormView, RedirectView
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.views import generic
from django.contrib.auth.models import User
from django.contrib.auth import REDIRECT_FIELD_NAME, login as auth_login, logout as auth_logout
from django.utils.decorators import method_decorator
from django.views.decorators.cache import never_cache
from django.views.decorators.csrf import csrf_protect
from django.views.decorators.debug import sensitive_post_parameters
from django.utils.http import is_safe_url
from django.contrib.auth.mixins import LoginRequiredMixin
# from .forms import CommentForm
from django.views.generic.edit import CreateView
from blog.models import Comment
# Create your views here.
class BlogListView(ListView):
    model = Post
    template_name = 'home.html'

class BlogDetailView(DetailView):
    model = Post
    template_name = 'post_detail.html'

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     qs = Comment.objects.filter(post=self.kwargs.get('pk'), active=True)
    #     context['comments'] = qs.order_by('-created_on')
    #     context['comment_form'] = CommentForm()
    #     return context


class BlogCreateview(CreateView):
    model = Post
    template_name = 'post_new.html'
    fields = ['title', 'author', 'body']

class BlogUpdateView(UpdateView):
    model = Post
    template_name = 'post_edit.html'
    fields = ['title', 'body', ]

class BlogDeleteView(DeleteView):
    model = Post
    template_name = 'post_delete.html'
    success_url = reverse_lazy('home')

class BlogSignUpView(generic.CreateView):
    model = Post
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'sign_up.html'

    def form_valid(self, form):
        return super(BlogSignUpView, self).form_valid(form)

class LoginView(FormView):
    model = Post
    success_url = reverse_lazy('home')
    template_name = 'login.html'
    form_class = AuthenticationForm

    @method_decorator(sensitive_post_parameters('password'))
    @method_decorator(csrf_protect)
    @method_decorator(never_cache)

    def dispatch(self, request, *args, **kwargs):
        # sets a test cookie to make sure the user has cookies enabled
        request.session.set_test_cookie()

        return super(LoginView, self).dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        auth_login(self.request, form.get_user())

        # If the test cookie worked, go ahead and delete it since its no longer needed
        if self.request.session.test_cookie_worked():
            self.request.session.delete_test_cookie()

        return super(LoginView, self).form_valid(form)

    


class LogoutView(RedirectView):
    """
    provides users the ability to logout"

    """
    url = '/login/'
    success_url = reverse_lazy('login')

    def get(self, request, *args, **kwargs):
        auth_logout(request)
        return super(LogoutView, self).get(request, *args, **kwargs)


class CommentCreateView(LoginRequiredMixin, CreateView):
    model = Comment
    template_name = 'post-detail.html'
    fields = [ 'post', 'body']
    success_url = reverse_lazy('post-detail')
    
    def get_success_url(self):
        return reverse_lazy('post-detail', kwargs={'pk': self.object.pk})
  
    
    

    