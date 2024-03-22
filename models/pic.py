from odoo import models, fields

class Mitra(models.Model):
    _name = "humanitarian.pic"
    _description = 'PIC'

    pic_id = fields.Many2one('humanitarian.sitrep', string='ID PIC')
    pic = fields.Char(string='PIC')