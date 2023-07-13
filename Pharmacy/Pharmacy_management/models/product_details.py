from odoo import models,fields

class ProductDetails(models.Model):
    _name = 'product.details'


    M_products_id = fields.Many2one("products",string="select product")
    M_products_company = fields.Many2one("products.company", string="select company")
    product_description = fields.Text(string="Enter Description")
    product_price = fields.Integer(string="Enter price")
    product_mfg_date = fields.Date(string="Enter manufacturing date")
    product_exp_date = fields.Date(string="Enter expiring date")
    product_power = fields.Float(string="Enter power")
    product_image = fields.Image(string="Image")
    Medicine_product_type_ids = fields.Many2one("product.types",string="select")
