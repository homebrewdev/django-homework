from django.urls import path
from blog import views
import blog.views

urlpatterns = [
    path('blog/', views.post_list, name = 'post_list'),
    path('', views.post_list, name = 'post_list'),
    path('add_spend/', views.add_spend, name = 'add_spend'),
    path('spends-view/', views.spends_view_url, name='view_spends'),
    path('spends-list/', blog.views.ListSpendView.as_view(), name='blog/spends-list'),
]