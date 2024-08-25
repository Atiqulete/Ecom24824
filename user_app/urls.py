from django.urls import path
from user_app.views import register,login_page,logout_view,profile,profileupdate

urlpatterns = [
    path('register/',register,name='register'),
    path('login_page/',login_page,name='login_page'),
    path('logout/',logout_view,name='logout_view'),
    path('profile/',profile,name='profile'),
    path('profile/update/',profileupdate,name='profileupdate-page'),
]
