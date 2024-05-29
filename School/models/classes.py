from odoo import fields, models, api




class Class(models.Model):

    _name = 'school_class'
    _description = 'Class'

    name = fields.Char(string='Subject Name', required=True)
    teacher_id = fields.Many2one('res.partner', string='Class Teacher')
    new_gender = fields.Selection(related='teacher_id.new_gender')
    age = fields.Integer(related='teacher_id.age')

    student_ids = fields.One2many('res.partner', 'class_id', string='Students')











