from django.urls import path

from bookapp import views

urlpatterns = [
    path("create_book", views.CreateBook, name='createbook'),
    path("author/", views.Create_Author, name='author'),
    path("admin_list",views.listBook,name='book_list'),
    path("detailsView/<int:book_id>/", views.detailsView, name='Details'),
    path("updateView/<int:book_id>/", views.updateBook, name='Update'),
    path('deleteView/<int:book_id>/', views.deleteView, name='delete'),
    path('index/', views.index),
    path('search/', views.search_book, name='search'),

]
