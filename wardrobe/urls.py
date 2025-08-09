from django.urls import path
from . import views

urlpatterns = [
    path('', views.shop, name='shop'),
    path('item/<int:item_id>/', views.clothing_detail, name='clothing_detail'),
    path('mannequin/', views.mannequin, name='mannequin'),
]
