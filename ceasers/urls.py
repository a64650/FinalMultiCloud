from django.urls import path, include
from ceasers import views

urlpatterns = [
    path('', views.options, name="options"),
    path('options/encrypt', views.encrypt, name="ceaseren"),
    path('options/decrypt', views.decrypt, name="ceaserdec")
]