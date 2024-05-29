from odoo import fields, api, models


class MasterEducation(models.Model):

    _name = 'master.education'
    _description = 'Master Education'
    _rec_name = 'class_id'

    class_id = fields.Many2one('new.class')
    section_id = fields.Many2one('new.section', ondelete='cascade')
    subject_ids = fields.Many2many('new.subject')