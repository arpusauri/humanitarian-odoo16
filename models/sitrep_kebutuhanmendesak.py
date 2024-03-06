from odoo import models, fields

class KebutuhanMendesak(models.Model):
    _name = "humanitarian.kebutuhan_mendesak"
    _description = 'Kebutuhan Mendesak'

    kebutuhan_mendesak = fields.Char(string="Kebutuhan Mendesak")
    site_id = fields.Many2one('humanitarian.sitrep', string='Situation')
    jumlah = fields.Integer(string="Jumlah")
    satuan = fields.Char(string="Satuan")