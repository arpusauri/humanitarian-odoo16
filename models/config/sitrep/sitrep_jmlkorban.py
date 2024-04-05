from odoo import models, fields

class JumlahKorbanJiwa(models.Model):
    _name = "humanitarian.sitrep_jmlkorban"
    _description = 'Jumlah Korban Jiwa'

    jenis_korban_jiwa = fields.Char(string="Jenis Korban Jiwa")
    korban_site_id = fields.Many2one('humanitarian.humanitarian_sitrep', string='Situation ID')
    jumlah = fields.Integer(string="Jumlah")