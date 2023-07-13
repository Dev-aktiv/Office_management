from odoo import models,fields

class Products(models.Model):
    _name = "products"
    _rec_name = "products"
    products = fields.Char(string="Enter product")