from django.urls import path
from .view import home, create,update, detail, delete


urlpatterns = [
    path('',home, name="home" ),
    path('create/', create, name="create"),
    path('update/<str:id>/', update, name="update"),
    path('detail/<int:detail_id>/', detail, name="detail"),
    path('delete/<str:id>/', delete, name="delete"),
]
