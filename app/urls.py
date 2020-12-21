from django.urls import path
from .view import home, create,update


urlpatterns = [
    path('',home, name="home" ),
    path('create/', create, name="create"),
    path('update/<int:id>/', create, name="update")
]
