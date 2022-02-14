from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('pogs/', views.PogList.as_view(), name='pogs_index'),
    path('pogs/new/', views.PogCreate.as_view(), name='pogs_create'),
    path('pogs/<int:pk>/update/', views.PogUpdate.as_view(), name='pogs_update'),
    path('pogs/<int:pk>/delete/', views.PogDelete.as_view(), name='pogs_delete'),
    # path('pogs/', views.index, name='index'),
    path('pogs/<int:pog_id>', views.show, name='show')
]