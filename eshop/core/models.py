from django.db import models

# Create your models here.

# following the database schema of zen-cart
# https://www.zen-cart.com/wiki/index.php/Developers_-_Database_Schema


class Product(models.Model):

	# a few related tables designed by zen-cart are combined here
	# TODO: will separating them into different models improve overall speed?
	# Note: use value_list to select only desired columns

	# zen-cart table products
	# https://www.zen-cart.com/wiki/index.php/Table_products#Table_Details

	

	product_id = models.AutoField(primary_key=True)
	product_date_added = models.DateTimeField(auto_now_add=True)
	#product_status = models.

	product_name = models.CharField(max_length=200)
	price = models.DecimalField(max_digits=10, decimal_places=2)

	time_created = models.DateTimeField(auto_now_add=True)
