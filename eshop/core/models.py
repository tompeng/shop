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

	PRODUCT_STATUS_ACTIVE = 100
	PRODUCT_STATUS_INACTIVE = 101
	PRODUCT_STATUS_COMING_SOON = 102
	PRODUCT_STATUS_SOLD_OUT = 103
	PRODUCT_STATUS_CHOICES = (
		(PRODUCT_STATUS_ACTIVE, 'active'),
		(PRODUCT_STATUS_INACTIVE, 'inactive'),
		(PRODUCT_STATUS_COMING_SOON, 'coming soon'),
		(PRODUCT_STATUS_SOLD_OUT, 'sold out'),
	)
	product_status = models.IntegerField(choices=PRODUCT_STATUS_CHOICES, default=PRODUCT_STATUS_ACTIVE, db_index=True)

	product_date_added = models.DateTimeField(auto_now_add=True)
	product_last_modified = models.DateTimeField(auto_now=True, blank=True, null=True)
	product_date_available = models.DateTimeField(blank=True, null=True)

	# product_type =
	product_quantity = models.FloatField(blank=True, null=True)
	# product_model =
	product_image = models.ImageField(blank=True, upload_to='images/product_images/')
	product_price = models.DecimalField(max_digits=10, decimal_places=4, default=0)
	product_is_virtual = models.BooleanField(default=False)
	product_weight = models.DecimalField(blank=True, max_digits=10, decimal_places=2, null=True)
	product_tax_class = models.BooleanField(default=True)  # Note: the actual tax is far more complicated than this
	product_ordered_count = models.IntegerField(default=0, editable=False)
	product_quantity_order_min = models.FloatField(blank=True, null=True)
	product_quantity_order_units = models.FloatField(blank=True, null=True)
	product_is_free = models.BooleanField(default=False)
	product_quantity_order_max = models.FloatField(default=0)
	product_sort_order = models.IntegerField(default=0)

	PRODUCT_DISCOUNT_TYPE_NONE = 200
	PRODUCT_DISCOUNT_TYPE_PERCENTAGE = 201
	PRODUCT_DISCOUNT_TYPE_ACTUAL_PRICE = 202
	PRODUCT_DISCOUNT_TYPE_AMOUNT_OFF_PRICE = 203
	PRODUCT_DISCOUNT_TYPE_CHOICES = (
		(PRODUCT_DISCOUNT_TYPE_NONE, 'none'),
		(PRODUCT_DISCOUNT_TYPE_PERCENTAGE, 'percentage discount'),
		(PRODUCT_DISCOUNT_TYPE_ACTUAL_PRICE, 'actual price'),
		(PRODUCT_DISCOUNT_TYPE_AMOUNT_OFF_PRICE, 'amount off discount'),
	)
	PRODUCT_DISCOUNT_TYPE = models.IntegerField(choices=PRODUCT_DISCOUNT_TYPE_CHOICES, default=PRODUCT_DISCOUNT_TYPE_NONE)

	product_final_price = models.DecimalField(max_digits=10, decimal_places=4, default=0, db_index=True)

	# zen-cart table products_description
	# https://www.zen-cart.com/wiki/index.php/Table_products_description

	product_name = models.CharField(max_length=64, db_index=True)
	product_description = models.TextField(blank=True)
	product_url = models.URLField(blank=True)
	product_viewed_count = models.IntegerField(default=0, editable=False)

	# Foreign Keys?
	# manufacturer_id =
	# categories_id =
	# language_id =

