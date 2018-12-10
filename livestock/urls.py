from django.urls import path, include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('LiveStock', views.LiveStockView)
router.register('TypeofLiveStock', views.TypesofLiveStockView)
router.register('Suit', views.SuitView)
router.register('Sex', views.SexView)
urlpatterns = [
    path('', include(router.urls))
]