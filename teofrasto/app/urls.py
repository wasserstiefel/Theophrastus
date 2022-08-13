from django.urls import path

from . import views

urlpatterns = [
    path('architects/<int:id>/', views.Architects),
    path('architects',views.Architect_List),
    path('firms', views.Firm_List),
    path('firms/<int:id>/', views.Firms),
    path('projects', views.Project_List),
    path('projects/<int:id>/', views.Projects),
    path('clients', views.Client_List),
    path('clients/<int:id>/', views.Clients)
    ]
