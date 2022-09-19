from distutils.log import Log
from re import A
from django.urls import path
from .views import Home, Books, Favourite, Login, Signup, BookDetails, AddToFav

urlpatterns = [
        path('', Home, name='home'),
        path('books/', Books, name='books'),
        path('favourite/', Favourite, name='favourite'),
        path('add_to_fav/<str:id>', AddToFav, name='add_to_fav'),
        path('login/', Login, name='login'),
        path('signup/', Signup, name='signup'),
        path('book_details/<str:id>', BookDetails, name='book_details'),
]