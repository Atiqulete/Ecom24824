from django.urls import path
from website.views import index,contact,pro_deta

urlpatterns = [
    path('',index,name='index'),
    path('contact/',contact,name='contact'),
    path('pro_deta/<int:pk>/',pro_deta,name='pro_deta'),
    
]
