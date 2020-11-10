from django.urls import path
from shop import views
from django.conf.urls.static import static
from DJ_diplom import settings

app_name = 'shop'

urlpatterns = [
    path('', views.IndexArticle.as_view(), name='index'),            # views.index_view, name='homepage'),
    path('catalog', views.catalog_view, name='product_list'),
    path('<slug:category_slug>/', views.product_list, name='product_list_by_category'),
    path('<int:id>/<slug:slug>/', views.product_detail, name='product_detail')
]

