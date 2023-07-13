from odoo import models,fields

class EmployeeManage(models.Model):
    _name = 'employee.manage'

    designation_type = fields.Selection([('manager','Manager'),('operator','Operator'),('marketing','Marketing')])
    name = fields.Char(string="Enter the name")
    address = fields.Text(string="Enter The Address")
    email = fields.Char(string="Enter The email-id")
    mobile = fields.Integer(string="Enter The mobile")
    gender = fields.Selection([('male','Male'),('female','Female')])
    image = fields.Image(string="Upload Image")
    date_of_birthday = fields.Date()
    age = fields.Integer(string="Enter your age")
    Emp_skill = fields.Many2many("skills", "emp_skill_rel", "emp_id", "skill_id", string="select skill")