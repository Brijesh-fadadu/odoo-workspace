from odoo import fields, models


# class New_Student(models.Model):
#     _name = 'classic.student'
#     _inherit = 'res.partner'
#
#     details = fields.Char(string='Details')
#

class Class(models.Model):
    _name = 'school_management.class'
    _description = 'Class'

    name = fields.Char(string='Name', required=True)
    teacher_id = fields.Many2one('school_management.teacher', string='Class Teacher')


