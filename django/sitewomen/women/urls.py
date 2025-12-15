from django.urls import path
from women import views

urlpatterns = [path('', views.index, name='home'),
							 path('cats/<int:cat_id>/', views.categories, name='cats_id'),
							 path('cats/<slug:cat_slug>', views.cat_by_slug, name='cats'),
							 path('get/', views.get_request),
							 path('archive/<int:year>/', views.archive, name='archive'),
							 path('about/', views.about, name='about'),
							 path('post/<int:post_id>', views.show_post, name='post'),
							 path('addpage/', views.addpage, name='add_page'),
							 path('contact/', views.contact, name='contact'),
							 path('login/', views.login, name='login'),
							 path('categories/<int:cat_id>', views.show_category, name='category')
							 ]