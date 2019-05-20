from django.db import models
from django.utils import timezone

class ShopInfo(models.Model):
    shopid = models.CharField(max_length = 20)
    product_id = models.CharField(max_length = 20)
    pub_time = models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return self.shopid
