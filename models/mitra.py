from odoo import models, fields

class Mitra(models.Model):
    _name = "humanitarian.mitra"
    _description = 'Mitra'

    mitra = fields.Char(string="Mitra")