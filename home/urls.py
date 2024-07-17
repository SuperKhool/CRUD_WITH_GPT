from django.urls import path
from . import views

urlpatterns  = [
    path('',views.home,name='home'),
    path('add/',views.add_employe,name="add_employe"),
    path('edit/<int:id>/',views.edit_employe,name="edit_employe"),
    path('<int:id>/',views.delete_employe,name='delete_employe'),
    
]
