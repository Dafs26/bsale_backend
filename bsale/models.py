from django.db import models

# Create your models here.

class Category(models.Model):
	name = models.CharField(max_length=250)

	def __str__(self):
		return self.name

class Product(models.Model):
	name = models.CharField(max_length=50)
	url_image = models.ImageField(upload_to='products')
	price = models.DecimalField(max_digits=8, decimal_places=1)
	discount = models.IntegerField()
	category = models.ForeignKey(Category, on_delete=models.CASCADE)

	def __str__(self):
		return self.name