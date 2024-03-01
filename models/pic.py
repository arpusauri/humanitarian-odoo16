from odoo import models, fields

class Mitra(models.Model):
    _name = "humanitarian.pic"
    _description = 'PIC'

    pic = fields.Char(string="PIC")