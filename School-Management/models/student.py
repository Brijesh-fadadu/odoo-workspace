from odoo import fields, models


class Student(models.Model):
    _name = 'school_management.student'
    _description = 'student'

    name = fields.Many2one('res.partner', string='Name', required=True)
    email = fields.Char(related='name.email')
    age = fields.Integer(string='Age')
    gender = fields.Selection([('male', 'Male'), ('female', 'Female')])
    class_id = fields.Many2one('school_management.class', string='Class')












