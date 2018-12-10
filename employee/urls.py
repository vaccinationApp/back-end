from django.urls import path, include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('Department', views.DepartmentView)
router.register('Employee', views.EmployeeView)
router.register('EmployeeType', views.EmployeeTypeView)
urlpatterns = [
    path('', include(router.urls))
]