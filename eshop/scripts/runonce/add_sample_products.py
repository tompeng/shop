# Run it like this:
# python manage.py shell < scripts/runonce/add_sample_products.py

from core.models import Product

products_info = [
	{'name': 'sample sunglasses',
	 'price': 50.00,
	 'description': 'very good sunglasses'},

	{'name': 'sample book',
	 'price': 150.00,
	 'description': 'very good book'},

	{'name': 'sample blanket',
	 'price': 50.00,
	 'description': 'very good blanket'},

	{'name': 'sample chicken',
	 'price': 50.00,
	 'description': 'very good chicken'},

	{'name': 'sample fishing pole',
	 'price': 50.00,
	 'description': 'very good fishing pole'},
]

for product_info in products_info:
	Product.objects.create(name=product_info['name'], price=product_info['price'],
	                       description=product_info['description'])

