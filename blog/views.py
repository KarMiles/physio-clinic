# Imports
# 3rd party:
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
from django.shortcuts import render, get_object_or_404
from django.views import generic, View
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy, reverse
from django.utils.text import slugify
from django.contrib.auth.mixins import AccessMixin
from django.contrib import messages

# Internal:
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
from .models import Post
from .forms import CommentForm, PostForm
from helpers.views import StaffRequiredMixin


# Views for blog app




class CreatePost(generic.CreateView):
    """
    A view to create a post
    Args:
        CreateView: class based view
    Returns:
        Render of post form with success message and context
    """
    template_name = "post_create.html"
    form_class = PostForm
    success_url = reverse_lazy('blog_home')

    def form_valid(self, form):
        """
        Set post author and slug to self instances
        Send confirmation message
        Returns form
        Args:
            self (object): self.
            form (object): form.
        Returns:
            The form
        """
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


class EditPost(StaffRequiredMixin, generic.UpdateView):
    """
    A view to edit a post
    Args:
        StaffRequiredMixin
        UpdateView: class based view
    Returns:
        Render of updated post with success message
    """
    template_name = "post_create.html"
    form_class = PostForm
    queryset = Post.objects.all()

    def form_valid(self, form):
        """
        Set post author and slug to self instances
        Send confirmation message
        Returns form
        Args:
            self (object): self.
            form (object): form.
        Returns:
            The form
        """
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


class DeletePost(StaffRequiredMixin, generic.DeleteView):
    """
    A view to delete a post
    Args:
        StaffRequiredMixin
        DeleteView: generic class based view
    Returns:
        Request confirmation of post deletion
        Redirect home after delete
    """
    success_url = reverse_lazy('blog_home')
    queryset = Post.objects.all()
    template_name = 'post_confirm_delete.html'

    def delete(self, request, *args, **kwargs):
        """
        Call the delete() method on the fetched object,
        then redirect to the success URL
        and show confirmation message.
        """
        self.object = self.get_object()
        success_url = self.get_success_url()
        self.object.delete()

        messages.add_message(
            self.request,
            messages.INFO,
            'Post deleted successfully!')

        return HttpResponseRedirect(success_url)


class PostList(generic.ListView):
    """
    A view to show posts
    Args:
        UpdateView: class based view
    Returns:
        Render main page with paginated list of posts
        Posts ordered by priority
        Non-staff users see live posts only
        Staff users see live and draft posts
    """
    model = Post
    template_name = "index.html"
    paginate_by = 3
    
    def get_queryset(self):
        if self.request.user.is_staff:
            return Post.objects.order_by("priority")
        else:
            return Post.objects.filter(status=1).order_by("priority")


class PostDetail(View):
    """
    A view to show posts
    Args:
        View: class based view
    Returns:
        Render post details
    """
    def get(self, request, slug):

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

    def post(self, request, slug):

        queryset = self.get_queryset()
        post = get_object_or_404(queryset, slug=slug)
        comments = post.comments.filter(approved=True).order_by("-created_on")
        liked = False
        if post.likes.filter(id=self.request.user.id).exists():
            liked = True

        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            comment_form.instance.author = request.user.username
            author = comment_form.instance.author
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
                "author": author,
                "success": 'Comment sent for approval'
            },
        )

    def get_queryset(self):
        if self.request.user.is_staff:
            return Post.objects.order_by("priority")
        else:
            return Post.objects.filter(status=1).order_by("priority")


class PostLike(View):
    """
    A view to show likes on posts
    Args:
        View: class based view
    Returns:
        Flips between adding and removing likes
    """

    def post(self, request, slug):
        post = get_object_or_404(Post, slug=slug)
        if post.likes.filter(id=request.user.id).exists():
            post.likes.remove(request.user)
        else:
            post.likes.add(request.user)

        return HttpResponseRedirect(reverse('post_detail', args=[slug]))
