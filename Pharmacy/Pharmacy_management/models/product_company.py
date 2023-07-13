from odoo import models,fields

class Product_company(models.Model):
    _name = "products.company"
    _rec_name = "products_company"
    products_company = fields.Char(string="Enter company")