from django.db import models
from django.utils import timezone

class ShopInfo(models.Model):
    shopid = models.CharField(max_length = 20)
    product1id = models.CharField(max_length = 20)
    product2id = models.CharField(max_length = 20)
    product3id = models.CharField(max_length = 20)
    pub_time = models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return self.shopid
