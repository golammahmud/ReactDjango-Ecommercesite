from django.contrib import admin
from .models import Product,Category,ProductImage,ProductFeatures


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('avatar_tag','id','title','parent','slug','created_at')
    list_display_links = ('id','title')


class ProductFeatureAdmin(admin.StackedInline):
    model = ProductFeatures
    
@admin.register(ProductImage)
class ImageAdmin(admin.ModelAdmin):
     list_display =('product','images')

class ProductImageAdmin(admin.StackedInline):
    model = ProductImage

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    inlines=[ProductImageAdmin,ProductFeatureAdmin]
    list_display = ('product_avatar_tag','id','title','price','category','created_at')
    list_display_links = ('id','title')




