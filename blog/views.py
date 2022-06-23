from django.shortcuts import render


# Views

class PostList(generic.ListView):
    model = PostList
    queryset = Post.objects.filter(status=1).order_by("-priority")
    template_name = "index.html"
    paginate_by = 3


