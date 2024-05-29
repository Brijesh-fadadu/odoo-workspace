from odoo import fields, models, api


class NewClass(models.Model):
    _name = 'new.class'
    _description = 'New Class'
    _rec_name = 'class_name'

    class_name = fields.Char(string='Standard Name')


class NewSubject(models.Model):
    _name = 'new.subject'
    _description = 'New Subject'
    _rec_name = 'new_subject'

    new_subject = fields.Char(string='Subject Name')


class NewSection(models.Model):
    _name = 'new.section'
    _description = 'New Section'
    _rec_name = 'new_section'

    new_section = fields.Char(string='Section', ondelete='cascade')