from django.urls import path, include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()

router.register('Village', views.VillageView)
router.register('RuralDistrict',views.RuralDistrictView)
router.register('Region', views.RegionView)
router.register('Oblast', views.OblastView)
router.register('Country', views.CountryView)
router.register('Farmer', views.FarmerView)
urlpatterns = [
    path('', include(router.urls))
]