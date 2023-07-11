from odoo import models,fields

class AttendanceInfo(models.Model):
    _name = 'attendance.info'

    employee_name = fields.Char("Enter employee name")
    check_in = fields.Datetime()
    check_out = fields.Datetime()
    over_time = fields.Datetime()
    leave_request = fields.Char("Enter the request")
    absent_date = fields.Date()
