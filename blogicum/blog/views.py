"""Views of blog app."""
from django.shortcuts import render, get_object_or_404
from django.http import Http404
from django.utils import timezone
from django.views.generic import ListView

from .models import Post, Category


class IndexView(ListView):
    model = Post
    queryset = Post.objects.select_related('category').filter(
        is_published=True,
        pub_date__lte=timezone.now(),
        category__is_published=True
    )
    template_name = 'blog/index.html'
    context_object_name = 'post_list'
    paginate_by = 5


def post_detail(request, post_id):
    post = get_object_or_404(
        Post.objects.select_related('category'),
        pk=post_id,
        is_published=True,
        pub_date__lte=timezone.now(),
        category__is_published=True
    )
    return render(request, 'blog/detail.html', {'post': post})


class CategoryListView(ListView):
    model = Post
    template_name = 'blog/category.html'
    context_object_name = 'post_list'

    def get_queryset(self):
        slug = self.kwargs['category_slug']
        category = get_object_or_404(Category, slug=slug)
        if not category.is_published:
            raise Http404(f'Категория с slug = {slug} не существует')
        return Post.objects.filter(
            category=category,
            is_published=True,
            pub_date__lte=timezone.now()
        )

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        slug = self.kwargs['category_slug']
        context['category'] = get_object_or_404(Category, slug=slug)
        return context
