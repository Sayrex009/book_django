from django.contrib import admin
from django.urls import path
from app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('books/', views.get_book_list),
    path('authors/', views.get_author_list),
    path('categories/', views.get_category_list),
    path('comments/', views.get_comment_list),
    path('users/', views.get_user_list),
]
