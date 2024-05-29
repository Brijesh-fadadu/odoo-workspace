from odoo import fields, models



class Teacher(models.Model):
    _name = 'school_management.teacher'
    _description = 'Teacher'


    name = fields.Char(string='Name', required=True)
    age = fields.Integer(string='Age')
    gender = fields.Selection([('male', 'Male'), ('female', 'Female')])
    subject_taught = fields.Char(string='Subject Taught')
    class_ids = fields.One2many('school_management.class', 'teacher_id', string='Class Taught')
    is_teacher = fields.Boolean(string="Is teacher")
