from django.urls import path

from . import views

app_name = 'app'

urlpatterns = [
    path('', views.SearchCNPJView.as_view(), name='home'),
    path('search/', views.SearchCNPJResultView.as_view(), name='search')
]

