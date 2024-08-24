from django.urls import path
from user_app.views import register,login_page,logout_view

urlpatterns = [
    path('register/',register,name='register'),
    path('login_page/',login_page,name='login_page'),
    path('logout/',logout_view,name='logout_view'),
]
