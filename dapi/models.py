from django.db import models

from io import BytesIO
from django.core.files import File
from PIL import Image
from django.utils.safestring import mark_safe
from django.template.defaultfilters import truncatechars
from django.db.models.signals import pre_save
from django.db.models import signals
from django.utils.text import  slugify
from django.dispatch import receiver
from django.urls import reverse
from rdshop.util import unique_slug_generator



class Category(models.Model):
    width=200
    height=200
    parent = models.ForeignKey('self', on_delete=models.CASCADE,related_name='child' ,null=True, blank=True)
    slug=models.SlugField(max_length=150,unique=True, null=True,default=None,blank=True)
    title=models.CharField(max_length=150,unique=True,default=None,null=False)
    image = models.ImageField(upload_to='product/category/images',default='product/no-image.jpg' ,verbose_name='image' ,width_field='width',height_field='height')
    created_at =models.DateTimeField(auto_now_add=True)
    is_featured=models.BooleanField(default=False)
    
    def __str__(self):
        return self.title
    class Meta:
        verbose_name_plural = 'categories'
        ordering = ('-id',)
    # @property
    # def short_description(self):
    #     return truncatechars(self.description,20)
    
    # @staticmethod
    # def post_images(self):
    #     return mark_safe('<img src="{image}" width="100" hieght="100" />' .format(self.image.url))
    # post_images.short_description='Profile picture'
    # post_images.alow_tags=True
    
    # def get_absolute_url(self):
    #     return reverse('products', kwargs={'slug': self.slug})
    
    
    def get_avatar(self):
        if not self.image:
            return 'product/no-image.jpg'
        return self.image.url
 
    # method to create a fake table field in read only mode
    def avatar_tag(self):
        return mark_safe('<img src="%s" width="110" height="110"  />' % self.get_avatar())
 
    avatar_tag.short_description = 'image'
    
def pre_save_receiver(sender, instance, *args, **kwargs): 
   if not instance.slug: 
       instance.slug = unique_slug_generator(instance) 

pre_save.connect(pre_save_receiver, sender = Category)



class Product(models.Model):
    width=600
    height=600
     
    category = models.ForeignKey(Category,related_name="products" ,on_delete=models.CASCADE)  
    variasions=models.ForeignKey('self',on_delete=models.CASCADE,related_name='children',blank=True,null=True)
    title = models.CharField(max_length=50)
    slug=models.SlugField(max_length=50,unique=True,null=True,blank=True)
    price = models.IntegerField()
    description = models.TextField(max_length=255)
    # feature=models.CharField(max_length=555 ,default=None)
    stock = models.CharField(max_length=150,null=True,blank=True)
    image = models.ImageField(upload_to='product/images',default='product/no-image.jpg' ,verbose_name='image' ,width_field='width',height_field='height')
    created_at =models.DateTimeField(auto_now_add=True)
    is_featured=models.BooleanField(default=False)
    def __str__(self):
        return self.title
    
    #set admin image avater
    # @property
    # def short_description(self):
    #     return truncatechars(self.description,20)
    # @staticmethod
    # def post_images(self):
    #     return mark_safe('<img src="{image}" width="100" hieght="100" />' .format(self.image.url))
    # post_images.short_description='Profile picture'
    # post_images.alow_tags=True
    
    
    #show product image avater on admin panel
       
    def get_avatar(self):
        if not self.image:
            return 'product/no-image.jpg'
        return self.image.url
 
    # method to create a fake table field in read only mode
    def product_avatar_tag(self):
        return mark_safe('<img src="%s" width="110" height="110"  />' % self.get_avatar())
 
    product_avatar_tag.short_description = 'image'
    
    def get_absolute_url(self):
        return reverse('categoris', kwargs={'slug': self.slug})
    
    
def create_slug(instance,new_slug=None):
    slug=slugify(instance.title) 
    if new_slug is not None:
        slug=new_slug
    qs=Product.objects.filter(slug=slug).order_by('-id')
    exists=qs.exists()
    if exists:
        new_slug="%S-%S"(slug,qs.first().id)
        return create_slug(instance,new_slug=new_slug)
    return slug


@receiver(pre_save, sender=Product)
def pre_save_receiver(sender, instance, *args, **kwargs):
   if not instance.slug:
       instance.slug = create_slug(instance)
pre_save.connect(pre_save_receiver,Product)



    
class ProductFeatures(models.Model):
    product=models.ForeignKey(Product,on_delete=models.CASCADE,related_name='features' ,default=None)
    feature=models.TextField(verbose_name='features',blank=True,null=True)
    def __str__(self):
        return self.product.title

class ProductImage(models.Model):
    width=400
    height=400
    product=models.ForeignKey(Product,related_name='products' , on_delete=models.CASCADE ,default=None)
    images=models.ImageField(upload_to='product/images',height_field='height',width_field='width')
    def __str__(self):
        return self.product.title

    