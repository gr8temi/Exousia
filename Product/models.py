from django.db import models
from django.urls import reverse
from django.conf import settings
# Create your models here.

class size(models.Model):
	"""
	Description: Model Description
	"""
	name= models.CharField(max_length=10)
	tag=models.CharField(max_length=3)

	def publish(self):
		self.save()

	def __str__(self):
		return self.name

class categories(models.Model):
	categories = models.CharField(max_length=20, null=True)
	catname = models.CharField(max_length=20)
	catImage = models.ImageField(upload_to='efe/', default='me.png')
	slug = models.SlugField(max_length=200,unique=True)
	# product = models.ManyToManyField(Product)
	def publish(self, *args, **kwargs):
		self.slug = slugify(self.catname)
		super(categories,self).save(*args, **kwargs)

	def __str__(self):
		return self.catname	

class brand(models.Model):
	"""
	Description: Model Description
	"""
	brand_name= models.CharField(max_length=20)
	brand_logo= models.ImageField(upload_to='media/product/brands')
	def publish(self):
		self.save()

	def __str__(self):
		return self.brand_name

class gender(models.Model):
	"""
	Description: Model Description
	"""
	gender= models.CharField(max_length=10)
	tags= models.CharField(max_length=1)

	def publish(self):
		self.save()

	def __str__(self):
		return self.gender


class Product(models.Model):
	"""
	Description: Model Description
	"""
	prod_image = models.ImageField(upload_to='image/products/')
	rearImage= models.ImageField(upload_to='image/products/', default='default.png', blank=True)
	frontImage= models.ImageField(upload_to='image/products/', default='default.png', blank=True)
	categories = models.ForeignKey(categories, on_delete=models.DO_NOTHING, blank=True, default=1)
	prodname = models.CharField(max_length=30, help_text='max of 30 characters')
	price = models.FloatField()
	sizes = models.ManyToManyField(size)
	numbers = models.PositiveIntegerField()
	description = models.TextField()
	weight= models.FloatField()
	Dimension= models.TextField()
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
	material = models.CharField(max_length=10)
	brand= models.ForeignKey(brand, on_delete=models.DO_NOTHING)
	gender= models.ForeignKey(gender,on_delete=models.DO_NOTHING, default=1)

	def publish(self):
		self.save()

	def __str__(self):
		return self.prodname

class States(models.Model):
	"""
	Description: Model Description
	"""
	state= models.CharField(max_length=50)
	def publish(self):
		self.save()

	def __str__(self):
		return self.state

class Lga(models.Model):
	lga = models.CharField(max_length=50)
	state = models.ForeignKey(States, on_delete=models.DO_NOTHING)
	def publish(self):
		self.save()

	def __str__(self):
		return self.lga

class cart(models.Model):
	product =  models.ForeignKey(Product, on_delete=models.DO_NOTHING)
	quantity = models.IntegerField(default=1)
	total = models.IntegerField(default=1)
	subtotal= models.IntegerField(default=1)
	shipping= models.FloatField()
	state = models.ForeignKey(States, on_delete=models.DO_NOTHING)
	lga = models.ForeignKey(Lga, on_delete=models.DO_NOTHING)

	def calc_total(self):
		total = quantity * product.price
		return total

	def publish(self):
		self.save()

	def __str__(self):
		return self.product