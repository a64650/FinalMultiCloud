from django.urls import path, include
from ceasers import views

urlpatterns = [
    path('', views.options, name="options"),
    path('/encrypt', views.encrypt, name="ceaseren"),
    path('/decrypt', views.decrypt, name="ceaserdec")
]