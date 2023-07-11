from odoo import models, fields


class HrManagement(models.Model):
    _name = 'hr.management'

    employees = fields.Char(string="Enter Employee name")
    employee_attendance = fields.Datetime()
    # employee_contact = fields.Integer(string="Enter the Number")
    employee_Pay = fields.Integer(string="")
    planning = fields.Text(string="Enter the Text here")
