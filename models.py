from odoo import models, fields

# create class
class RestaurantProduct(models.Model):

	_inherit = "product.template"
	_description = "organize the restaurant product"

	x_product_weight = fields.Integer("وزن المنتج")
	x_product_calerise = fields.Float("السعرات الحرارية للمنتج ")
	x_product_expired_date = fields.Date("تاريخ أنتهاء المنتج ")

