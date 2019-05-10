from django.urls import path
from blog import views

urlpatterns = [
    path('blog/', views.post_list, name = 'post_list'),
    path('', views.post_list, name = 'post_list'),
    path('spend/', views.spend_url, name = 'add_spend'),
]