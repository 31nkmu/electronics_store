from rest_framework.routers import DefaultRouter
from . import views


router = DefaultRouter()
router.register('', views.ElectronicViewSet, basename='electronic')

urlpatterns = router.urls