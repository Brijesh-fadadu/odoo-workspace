from odoo import fields, models, api
from odoo.exceptions import ValidationError


class GeneralFields(models.Model):

    _name = 'general.fields'
    _description = 'General Fields'

    text1 = fields.Char(string='Text', required=True, help='add any Text', placeholder="General", size=10)
    text2 = fields.Char(string='email')
    text3 = fields.Char(string='phone')
    text4 = fields.Char(string='url')
    text5 = fields.Char(string='badge')
    text6 = fields.Char(string='Copy to Clipboard')

    multiline_text = fields.Text(string='Multiline Text')


    #integer field
    n1 = fields.Integer(string='Integer')
    n3 = fields.Integer(string='Percentage Pie')
    n4 = fields.Integer(string='Progressbar')


    #Decimal field
    f1 = fields.Float(string='Float')
    f2 = fields.Float(string='Percentage')
    f3 = fields.Float(string='Percentage Pie', compute='_progress_bar')
    f4 = fields.Float(string='Progressbar', compute='_progress_bar')
    currency_id = fields.Many2one("res.currency", string='Currency')
    f5 = fields.Float(string='Monetary')


    #selection
    gender = fields.Selection([('male','Male'),('female','Female')], string='Gender')
    subjects = fields.Selection([('maths','Maths'),('science','Science'),('english','English')], string='Subjects')




    #boolean
    is_boolean = fields.Boolean(string='Checkbox')

    #date
    expiry_date = fields.Date(fields="Date")
    dt_datetime = fields.Datetime(string='Datetime')

    #files
    txt_file = fields.Binary(string='File')
    image = fields.Binary(string='Image')
    pdf = fields.Binary(string='PDF Viewer')
    sign = fields.Binary(string='Sign')

    #Relational Fields
    student_id = fields.Many2one('res.partner', domain="[('identity', '=', 'Student')]")
    student_age = fields.Integer(related='student_id.age', string="Age")
    subject_ids = fields.Many2many('new.subject','student_subject', string='Subjects')

    @api.onchange('student_id')
    def _subject_details(self):
        s_id = self.env['res.partner'].search([('id', '=', self.student_id.id)])
        print(s_id)
        mapped_data = s_id.mapped('new_subjects_ids.id')
        print(mapped_data)
        self.write({'subject_ids': [(6, 0, mapped_data)]})


    @api.depends('f2')
    def _progress_bar(self):
       progress = 0
       for rec in self:
           if rec.f1 < 0 or rec.f1 > 100:
               raise ValidationError("Please enter digit between 0 & 100")
           else:
               if rec.f1 <= 50 and rec.f1 > 0:
                   progress = 50
               elif rec.f1 == 100:
                   progress = 100
               rec.f4 = progress
               rec.f3 = progress







