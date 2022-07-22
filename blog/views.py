from django.shortcuts import render, get_object_or_404
from django.views import generic, View
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy, reverse
from django.utils.text import slugify
from django.contrib.auth.mixins import LoginRequiredMixin, AccessMixin
from django.contrib import messages

from .models import Post
from .forms import CommentForm, PostForm


# Views for blog app

class StaffRequiredMixin(AccessMixin):
    """Verify that the current user
    is authenticated as member of staff."""
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_staff:
            return self.handle_no_permission()
        return super().dispatch(request, *args, **kwargs)


class CreatePost(generic.CreateView):
    template_name = "create_post.html"
    form_class = PostForm
    success_url = reverse_lazy('blog_home')

    def form_valid(self, form):
        self.object = form.instance
        self.object.author = self.request.user
        self.object.slug = slugify(self.object.title)
        response = super().form_valid(form)
        messages.add_message(
            self.request,
            messages.INFO,
            'Post created successfully!')
        return response

    def get_success_url(self):
        return reverse('post_detail', args=[self.object.slug])


class EditPost(LoginRequiredMixin, StaffRequiredMixin, generic.UpdateView):
    template_name = "create_post.html"
    form_class = PostForm
    queryset = Post.objects.all()

    def form_valid(self, form):
        self.object = form.instance
        self.object.author = self.request.user
        self.object.slug = slugify(self.object.title)
        messages.add_message(
            self.request,
            messages.INFO,
            'Post submitted successfully!')
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('post_detail', args=[self.object.slug])


class DeletePost(LoginRequiredMixin, StaffRequiredMixin, generic.DeleteView):
    
    success_url = reverse_lazy('blog_home')
    queryset = Post.objects.all()
    template_name = 'post_confirm_delete.html'


class PostList(generic.ListView):
    model = Post
    template_name = "index.html"
    paginate_by = 3
    
    def get_queryset(self):
        if self.request.user.is_staff:
            return Post.objects.order_by("priority")
        else:
            return Post.objects.filter(status=1).order_by("priority")


class PostDetail(View):

    def get(self, request, slug, *args, **kwargs):

        queryset = self.get_queryset()
        post = get_object_or_404(queryset, slug=slug)
        comments = post.comments.filter(approved=True).order_by("created_on")
        liked = False
        if post.likes.filter(id=self.request.user.id).exists():
            liked = True

        return render(
            request,
            "post_detail.html",
            {
                "post": post,
                "comments": comments,
                "commented": False,
                "liked": liked,
                "comment_form": CommentForm()
            },
        )

    def post(self, request, slug, *args, **kwargs):

        queryset = self.get_queryset()
        post = get_object_or_404(queryset, slug=slug)
        comments = post.comments.filter(approved=True).order_by("-created_on")
        liked = False
        if post.likes.filter(id=self.request.user.id).exists():
            liked = True

        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            comment_form.instance.email = request.user.email
            comment_form.instance.name = request.user.username
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.save()
        else:
            comment_form = CommentForm()
        
        return render(
            request,
            "post_detail.html",
            {
                "post": post,
                "comments": comments,
                "commented": True,
                "comment_form": comment_form,
                "liked": liked,
                "success": 'Comment sent for approval'
            },
        )

    def get_queryset(self):
        if self.request.user.is_staff:
            return Post.objects.order_by("priority")
        else:
            return Post.objects.filter(status=1).order_by("priority")


class PostLike(View):

    def post(self, request, slug):
        post = get_object_or_404(Post, slug=slug)
        if post.likes.filter(id=request.user.id).exists():
            post.likes.remove(request.user)
        else:
            post.likes.add(request.user)

        return HttpResponseRedirect(reverse('post_detail', args=[slug]))
