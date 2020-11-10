from django.shortcuts import render, get_object_or_404
from shop.models import Category, Product, Article
from django.views.generic import ListView


# def index_view(request):
#
#     articles = Article.objects.prefetch_related('products')
#
#     context = {'articles': articles}
#
#     return render(request, 'shop/index.html', context)


class IndexArticle(ListView):
    template_name = 'shop/index.html'
    model = Article
    ordering = 'created'


def catalog_view(request):
    pass


def product_list(request):
    pass


def product_detail(request):
    pass
