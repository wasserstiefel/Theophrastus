from django.urls import path
from rest_framework.routers import DefaultRouter
from . import views
router  = DefaultRouter()
router.register('architects', views.ArchitectViewSet)
router.register('firms', views.FirmViewSet)
router.register('projects', views.ProjectViewSet)
router.register('clients', views.ClientViewSet)


urlpatterns = router.urls