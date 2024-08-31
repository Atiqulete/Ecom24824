from django.urls import path
from website.views import index,contact,pro_deta,about

urlpatterns = [
    path('',index,name='index'),
    path('contact/',contact,name='contact'),
    path('about/',about,name='about'),
    path('pro_deta/<int:pk>/',pro_deta,name='pro_deta'),
    
]
