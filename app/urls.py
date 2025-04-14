from . import views
from django.urls import path

urlpatterns = [
    path('',views.aaa,name="main"),
    path('hhh/',views.bbb,name="o"),
    path('login/',views.ccc,name="log"),
]