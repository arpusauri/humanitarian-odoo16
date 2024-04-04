from odoo import models, fields

class JenisKejadian(models.Model):
    _name = "humanitarian.humanitarian_jenis_kejadian"
    _description = 'Jenis Kejadian'
    _rec_name = "jenis_kejadian"

    jenis_kejadian = fields.Char(string="Jenis Kejadian")