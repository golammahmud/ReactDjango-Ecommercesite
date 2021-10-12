from django.shortcuts import render

from .serializers import ProductSerializer,CategorySerializer,ProductImageSerializer,ProductFeatureSerializers
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import Product,Category,ProductImage,ProductFeatures
from drf_multiple_model.views import FlatMultipleModelAPIView




class ProductViewSet(viewsets.ModelViewSet):

    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    
    
class ProductFeatureView(viewsets.ModelViewSet):
    queryset=ProductFeatures.objects.all()
    serializer_class=ProductFeatureSerializers


class ProductimagesViewSet(viewsets.ModelViewSet):

    queryset = ProductImage.objects.all()
    serializer_class = ProductImageSerializer
  
    # def get_queryset(self):
    #     """Combine queries from new, editor choice and popular"""
    #     new_qs = self.queryset.filter(new_place=True)[:self.slice_size]
    #     editor_qs = self.queryset.filter(editor_choice=True)[:self.slice_size]
    #     popular_qs = self.queryset.filter(popular=True)[:self.slice_size]

    #     return new_qs.union(editor_qs, popular_qs, all=True)


class CategoryViewSet(viewsets.ModelViewSet):

    queryset = Category.objects.filter(parent=None)
    serializer_class = CategorySerializer
  
# class ProductViewSet(FlatMultipleModelAPIView):
#     querylist = [
#            {
#             'queryset': Product.objects.all(),
#             'serializer_class': ProductSerializer,
            
#         },
#         {
#             'queryset': ProductImage.objects.filter(),
#             'serializer_class': ProductImageSerializer,
           
#         },
      
#     ]
    
   