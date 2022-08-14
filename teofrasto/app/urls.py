from django.urls import path

from . import views

urlpatterns = [
    path('architects/<int:id>/', views.Architects.as_view()),
    path('architects',views.ArchitectList.as_view()),
    path('firms', views.FirmList.as_view()),
    path('firms/<int:id>/', views.Firms.as_view()),
    path('projects', views.ProjectList.as_view()),
    path('projects/<int:id>/', views.Projects.as_view()),
    path('clients', views.ClientList.as_view()),
    path('clients/<int:id>/', views.Clients.as_view())
    ]
