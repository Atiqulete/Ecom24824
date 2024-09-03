from django.urls import path
from website.views import index,contact,pro_deta,about,product_search

urlpatterns = [
    path('',index,name='index'),
    path('contact/',contact,name='contact'),
    path('about/',about,name='about'),
    path('search/',product_search,name='product_search-page'),
    path('pro_deta/<int:pk>/',pro_deta,name='pro_deta'),
    
]