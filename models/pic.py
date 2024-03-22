from odoo import models, fields

class Mitra(models.Model):
    _name = "humanitarian.pic"
    _description = 'PIC'
    _rec_name = 'pic'

    pic_id = fields.Many2one('humanitarian.sitrep', string='ID PIC')
    pic = fields.Char(string='PIC')