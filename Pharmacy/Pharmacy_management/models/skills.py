from odoo import models,fields

class skills(models.Model):
    _name = "skills"
    _rec_name = "emp_skills"
    emp_skills = fields.Char(string="Enter product")