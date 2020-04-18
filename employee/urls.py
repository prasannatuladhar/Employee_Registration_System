from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('delete/<int:emp_id>',views.delete,name='delete'),
    path('add/',views.add,name='add'),
    path('edit/<int:emp_id>',views.edit,name='edit'),
]
