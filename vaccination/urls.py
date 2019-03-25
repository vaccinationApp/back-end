from django.urls import path, include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('Medicine', views.MedicineView)
router.register('Disease', views.DiseaseView)
router.register('Vaccination', views.VaccinationView)
router.register('BloodTest', views.BloodtestView)
router.register('Modeofapplication', views.BloodtestView)
router.register('TestMethod', views.TestMethodView)
router.register('TableVaccination',views.TableVaccinationView,basename='tablevac')
router.register('TableBloodTest',views.TableBloodtestView,basename='tableblood')
urlpatterns = [
    path('', include(router.urls))
]