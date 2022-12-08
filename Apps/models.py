from django.db import models
from django.contrib.auth.models import User
# Create your models here.
CATEGORY_CHOICES =(
    ('CR', 'Curd'),
    ('ML', 'Milk'),
    ('LS', 'Lassi'),
    ('MS', 'Milkshake'),
    ('PN', 'Paneer'),
    ('GH', 'Ghee'),
    ('CZ', 'Cheese'),
    ('IC', 'Ice-Creams'),
)
STATE_CHOICES = (
    ('Barisal Division', 'Barisal Division'),	
	('Chittagong Division', 'Chittagong Division'),
	('Dhaka Division', 'Dhaka Division'), 
	('Khulna Division', 'Khulna Division'), 	
	('Rajshahi Division', 'Rajshahi Division'), 	
	('Rangpur Division', 'Rangpur Division'), 
	('Sylhet Division', 'Sylhet Division') 
)
class Product(models.Model):
    title = models.CharField(max_length=100)
    selling_price = models.FloatField()
    discount_price = models.FloatField()
    description = models.TextField()
    compositions = models.TextField(default='')
    product_app = models.TextField(default='')
    category = models.CharField(max_length=2, choices=CATEGORY_CHOICES,)
    created_at = models.DateTimeField(auto_now_add=True)
    Product_image = models.ImageField(upload_to='products')

    def __str__(self):
        return self.title


class Customer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField( max_length=255)
    locality = models.CharField(max_length=200)
    city = models.CharField(max_length=50)
    mobile = models.IntegerField(default=0)
    zipcode = models.IntegerField()
    state = models.CharField(choices=STATE_CHOICES, max_length=100)

    def __str__(self):
        return self.name
    
class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    @property
    def total_cost(self):
        return self.quantity * self.product.discount_price
