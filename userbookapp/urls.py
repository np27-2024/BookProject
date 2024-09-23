from django.urls import path
from userbookapp import views

urlpatterns = [

    path("", views.UserlistBook, name='User_list_view'),
    path("userdetails/<int:book_id>/", views.UserdetailsView, name='User_book_details'),
    path('userindex/', views.User_index),
    path('usersearch/', views.User_search, name='User_search_view'),
    path('view_cart/', views.view_cart, name='view_cart'),
    path('add_to_cart/<int:book_id>/', views.add_to_cart, name='add_to_cart'),
    path('increase_quantity/<int:item_id>/', views.increase_quantity, name='increase_quantity'),
    path('decrease_quantity/<int:item_id>/', views.decrease_quantity, name='decrease_quantity'),
    path('remove/<int:item_id>/',views.remove_from_cart, name='remove_item'),
    path('create_checkout_session/',views.create_checkout_session, name='Checkout_session_Create'),
    path('success/', views.success, name='success'),
    path('cancel/',views.cancel, name='cancel')
]
