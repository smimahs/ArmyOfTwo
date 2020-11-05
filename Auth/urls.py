from django.urls import path
from . import views



urlpatterns = [
    path('index', views.index, name='index'),
    #path('signupemployee',views.signUpEmployee,name='signupemployee'),
    path('signup',views.signUp,name='signup'),
    path('signin',views.signIn,name='signin'),
    path('logout',views.logout,name='logout'),
    path('blog',views.blog,name='blog'),
    path('post/<slug:slug>',views.post),
    path('shop',views.shop,name='shop'),
    path('product/<slug:slug>',views.product),

]