from django.urls import path
from . import views


urlpatterns = [
    path("", views.view_cart, name="cart"),
    path("add/<int:game_id>", views.add_to_cart, name="add_to_cart"),
    path("edit/<int:game_id>", views.modify_cart, name="modify_cart"),
    path("delete/<int:game_id>", views.remove_from_cart, name="remove_from_cart"),
]
