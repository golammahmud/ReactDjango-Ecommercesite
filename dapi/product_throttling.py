from rest_framework.throttling import UserRateThrottle


class ProductRateThrottle(UserRateThrottle):
    scope='product'
    
    
class CategoryRateThrottle(UserRateThrottle):
    scope='product'