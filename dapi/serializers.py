from rest_framework import serializers
from .models import Product,Category,ProductImage,ProductFeatures



class ProductFeatureSerializers(serializers.HyperlinkedModelSerializer):
    
    class Meta:
        model=ProductFeatures
        fields=['feature']

class ProductImageSerializer(serializers.HyperlinkedModelSerializer):
    # products=ProductSerializer(many=True,read_only=True)
    class Meta:
        model = ProductImage
        # fields='__all__'
        fields=['id','images']
        # include='products'
        

class ProductSerializer(serializers.HyperlinkedModelSerializer):
 
    products=ProductImageSerializer(many=True, read_only=True)
    features=ProductFeatureSerializers(many=True, read_only=True)
    
    class Meta:
        model = Product
        # fields = '__all__'
        # include=['images']
        fields = ['id','url','title','slug','price','category','variasions','stock','description','image','is_featured' ,'created_at','products','features']
       


# class CategoryDetailsSerializers(serializers.HyperlinkedModelSerializer):
#     class Meta:
#         model=Category




class CategorySerializer(serializers.HyperlinkedModelSerializer):
    products = ProductSerializer(many=True,read_only=False)
    class Meta:
        model = Category
        fields = ['url','id','title','slug','parent','image','is_featured','created_at','products']
        # fields = '__all__'
        # include=['id','products']


        
