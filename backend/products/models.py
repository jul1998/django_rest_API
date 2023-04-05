from django.db import models

# Create your models here.

class Product(models.Model):
    title = models.CharField(max_length=120)
    description = models.TextField()
    price = models.DecimalField(decimal_places=2, max_digits=10000)
    summary = models.TextField(blank=True, null=True)
    featured = models.BooleanField(default=False)

    def __str__(self):
        return self.title

    @property
    def sale_price(self):
        return "%.2f" % (self.price * 2)
    
    def get_discount(self):
        return "122"