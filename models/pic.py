from odoo import models, fields

class Mitra(models.Model):
    _name = "humanitarian.pic"
    _description = 'PIC'
    _rec_name = 'pic'

    pic = fields.Char(String="PIC")