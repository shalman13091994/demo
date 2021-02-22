from django.urls import path
from.views import calc,add

urlpatterns=[
    path('',calc,name='calc2'),
    path('calculate',add,name='addi')
];