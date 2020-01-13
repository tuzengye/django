from django.conf.urls import url
from . import views

app_name='productapp'
urlpatterns=[
    url(r'^$', views.product_list, name='product_list'),
    # url(r'^$', views.ProductIndex.as_view(), name='product_list'),
    url(r'^product/(?P<pk>\d+)$', views.product_details, name='product_details'),
    url(r'^product/add/$',views.ProductAdd.as_view(),name='product_add')
]