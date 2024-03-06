from odoo import models, fields

class JumlahKorbanJiwa(models.Model):
    _name = "humanitarian.jml_korbanjiwa"
    _description = 'Jumlah Korban Jiwa'

    jenis_korban_jiwa = fields.Char(string="Jenis Korban Jiwa")
    site_id = fields.Many2one('humanitarian.sitrep', string='Situation')
    jumlah = fields.Integer(string="Jumlah")