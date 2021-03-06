from django.urls import path
from . import views

urlpatterns = [
	path('', views.index, name='index'),
	path('techtips', views.tips, name = 'tips'),
	path('about', views.about, name = 'about'),
	path('archive', views.archive, name = 'archive'),
	path('<int:post_id>/', views.post, name = 'post'),
	path('<int:post_id>/comment/', views.comment, name = 'comment'),
]
