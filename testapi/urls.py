
from django.urls import path,include
from rest_framework import routers
from testapi import views
from rest_framework.authtoken.views import obtain_auth_token
router = routers.DefaultRouter()
router.register('students', views.StudentViewSet)

urlpatterns = [
   
    path('', include(router.urls)),
    path('auth/', include('rest_framework.urls',namespace='rest_framework') ),
    path('api-token-auth/', obtain_auth_token, name='api_token_auth'),
]
