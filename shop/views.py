from django.shortcuts import render, get_object_or_404

from cart.forms import CartAddProductForm
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


def product_list(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    products = Product.objects.filter(available=True)
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)
    return render(request,
                  'shop/product/list.html',
                  {'category': category,
                   'categories': categories,
                   'products': products})


def product_detail(request, id, slug):
    # product = get_object_or_404(Product,
    #                             id=id,
    #                             slug=slug,
    #                             available=True)

    product = Product.objects.get(id=id, slug=slug)

    cart_product_form = CartAddProductForm()

    return render(request,
                  'shop/product/detail.html',
                  {'product': product,
                   'cart_product_form': cart_product_form})
