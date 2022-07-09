from django.shortcuts import render, get_object_or_404, reverse
from django.views import generic, View
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.utils.text import slugify

from .models import Post
from .forms import CommentForm, PostForm


# Views

# TODO add mixin demanding logging in (to post.author)

class CreatePost(generic.CreateView):
    template_name = "create_post.html"
    form_class = PostForm
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        post = form.instance
        post.author = self.request.user
        post.slug = slugify(post.title)
        # post.save()
        # super() relates to CreateView - higher class:
        return super().form_valid(form)


class EditPost(generic.UpdateView):
    template_name = "create_post.html"
    form_class = PostForm
    # success_url = reverse_lazy('home')
    queryset = Post.objects.all()

    def form_valid(self, form):
        post = form.instance
        post.author = self.request.user
        post.slug = slugify(post.title)
        # post.save()
        # super() relates to CreateView - higher class:
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('post_detail', args=[self.kwargs['slug']])


class PostList(generic.ListView):
    model = Post
    queryset = Post.objects.filter(status=1).order_by("priority")
    template_name = "index.html"
    paginate_by = 3


class PostDetail(View):

    def get(self, request, slug, *args, **kwargs):

        queryset = Post.objects.filter(status=1)
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

        queryset = Post.objects.filter(status=1)
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


class PostLike(View):

    def post(self, request, slug):
        post = get_object_or_404(Post, slug=slug)
        if post.likes.filter(id=request.user.id).exists():
            post.likes.remove(request.user)
        else:
            post.likes.add(request.user)

        return HttpResponseRedirect(reverse('post_detail', args=[slug]))
