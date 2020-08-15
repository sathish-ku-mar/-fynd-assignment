from django.urls import path,include

from .views import UserViewSet


urlpatterns = [
    path(r'signup/', UserViewSet.as_view({'post': 'create'}), name='signup'),
    path(r'login/', UserViewSet.as_view({'post': 'login'}), name='login'),
]