
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from dapi import views
from rest_framework_simplejwt.views import  TokenObtainPairView, TokenRefreshView
   
# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register('products', views.ProductViewSet,basename='products'), 
router.register('category', views.CategoryViewSet,basename='categoris' )
router.register('images', views.ProductimagesViewSet )
router.register('productfeature', views.ProductFeatureView)


# The API URLs are now determined automatically by the router.
urlpatterns = [
    path('', include(router.urls)),
    path('get_token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token_refresh/', TokenRefreshView.as_view(), name='token_refresh'),
  

]


