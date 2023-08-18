from django.urls import path
from .views import (AllCreateTodoView,DetailApiView,AllTodosView,UpdateApiView,DeleteApiView)

urlpatterns = [
    path('create/',AllCreateTodoView.as_view()),
    path('update/<int:pk>/',UpdateApiView.as_view()),
    path('delete/<int:pk>/',DeleteApiView.as_view()),
    path('detail/<int:pk>/',DetailApiView.as_view()),
    path('',AllTodosView.as_view())
]

