from django.urls import path

from . import views

urlpatterns = [
    path('architects',views.ArchitectList.as_view()),
    path('architects/<int:pk>/', views.Architects.as_view()),
    path('firms', views.FirmList.as_view()),
    path('firms/<int:pk>/', views.Firms.as_view()),
    path('projects', views.ProjectList.as_view()),
    path('projects/<int:pk>/', views.Projects.as_view()),
    path('clients', views.ClientList.as_view()),
    path('clients/<int:pk>/', views.Clients.as_view())
    ]
