from django.urls import path

from . import views

urlpatterns = [
    path('architects/<int:id>/', views.Architects),
    path('architects',views.Architect_List)
]
