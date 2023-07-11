from odoo import models,fields

class EmplyeeInfo(models.Model):
    _name = 'employee.info'

    name = fields.Char(string="Enter the name")
    address = fields.Text(string="Enter the Address here")
    email = fields.Char(string="Enter the email-id")
    mobile = fields.Integer(string="Enter the mobile")
    gender = fields.Selection([('male','Male'),('female','Female')])
    designation = fields.Char(string="Enter the Designation")
    image = fields.Image()
    date_of_birthday = fields.Date()

