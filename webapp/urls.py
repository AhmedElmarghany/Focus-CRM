from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path("signup/", views.register, name='signup'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('create-record/', views.create_record, name='createrecord'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('delete-account/', views.delete_account, name='deleteAccount'),
    path('view/<int:record_id>/', views.view_record, name='view_record'),
]