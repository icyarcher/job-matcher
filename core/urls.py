from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import JobViewSet, index
from . import views

router = DefaultRouter()
router.register(r'jobs', JobViewSet)

urlpatterns = [
    path('', views.index, name='index'),
    path('api/', include(router.urls)),
]
