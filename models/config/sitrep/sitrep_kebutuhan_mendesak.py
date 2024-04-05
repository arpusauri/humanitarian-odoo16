from odoo import models, fields

class KebutuhanMendesak(models.Model):
    _name = "humanitarian.sitrep_kebutuhan_mendesak"
    _description = 'Kebutuhan Mendesak'

    kebutuhan_mendesak = fields.Char(string="Kebutuhan Mendesak")
    kebutuhan_site_id = fields.Many2one('humanitarian.humanitarian_sitrep', string='Situation ID')
    jumlah = fields.Integer(string="Jumlah")
    satuan = fields.Char(string="Satuan")