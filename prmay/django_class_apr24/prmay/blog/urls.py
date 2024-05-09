from django.urls import path
from . import views
urlpatterns = [
    path('',views.blog1),
    path('/msg',views.msg),
]