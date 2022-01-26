from django.urls import path, re_path
from .  import views



urlpatterns = [
    path('', views.index, name="blog_index"),
    path('<int:pk>/', views.blog_detail, name="blog_detail"),
    path('<category>/', views.category, name="blog_category"),

]