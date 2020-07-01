from django.urls import path
from . import views


urlpatterns = [
    path('register',views.register,name = 'register'),
    path('login',views.login,name = 'login'),
   	path('view_books',views.view_books,name = 'view_books'),
   	path('profile',views.profile,name = 'profile'),
   	path('',views.view_books,name = 'view_books'),
   	path('buy_book/<int:bid>',views.buy_book,name = 'buy_book'),
   	path('return_book/<int:bid>',views.return_book,name = 'return_book'),
   	path('logout',views.logout,name = 'logout')
]
