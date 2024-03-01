from odoo import models, fields

class JenisKejadian(models.Model):
    _name = "humanitarian.jenis_kejadian"
    _description = 'Jenis Kejadian'

    jenis_kejadian = fields.Char(string="Jenis Kejadian")