from odoo import models,fields

class ProductTypes(models.Model):
    _name = "product.types"
    _rec_name = "P_product_type"
    P_product_type = fields.Char(string="Select type")
