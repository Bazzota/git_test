from django.urls import path
from women import views

urlpatterns = [path('', views.index, name='home'),
							 path('cats/<int:cat_id>/', views.categories, name='cats_id'),
							 path('cats/<slug:cat_slug>', views.cat_by_slug, name='cats'),
							 path('get/', views.get_request),
							 path('archive/<int:year>/', views.archive, name='archive'),
							 path('about/', views.about, name='about')
							 ]