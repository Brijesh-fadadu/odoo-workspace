from odoo import fields, models


class StudentComplaint(models.TransientModel):
    _name = 'student_complaint'
    _description = 'Student Complaint'

    name = fields.Many2one('res.partner', string='Name', required=True)
    email = fields.Char(string='Email', related='name.email')
    complaint = fields.Text(string='Complaint', required=True)