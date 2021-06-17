from django.contrib import admin
from django.urls import path
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('', views.home, name='home'),
    path('submitAddItem', views.submitAddItem, name='submitAddItem'),
    path('deleteItem/<int:id>', views.deleteItem, name="deleteItem"),
    path('updateItem/<int:id>', views.updateItem, name="updateItem"),
    path('updateItemFinal/<int:id>', views.updateItemFinal, name="updateItemFinal"),
    path('searchBar', views.searchBar, name="searchBar"),
]

urlpatterns += staticfiles_urlpatterns()