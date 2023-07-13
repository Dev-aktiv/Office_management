from odoo import models,fields

class TaskManage(models.Model):
    _name = 'task.manager'

    task_name = fields.Char(string="")
    task_team = fields.Char(string="")
    task_startDate = fields.Date()
    task_endDate = fields.Date()
    task_submissionDate = fields.Date()


