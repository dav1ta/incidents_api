from django.urls import (
    path,
    include,
)

from rest_framework.routers import DefaultRouter

from api import views


router = DefaultRouter()
router.register('incidents', views.IncidentViewset)
router.register('targets', views.TargeViewset)
router.register('cves', views.CveViewset)
router.register('incident-descriptions', views.DescriptionViewset)

app_name = 'api'

urlpatterns = [
    path('', include(router.urls)),
]
