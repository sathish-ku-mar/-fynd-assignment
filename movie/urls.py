from django.urls import path,include
from django.conf.urls import url

from .views import MovieViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'', MovieViewSet)


urlpatterns = [
]

urlpatterns += router.urls