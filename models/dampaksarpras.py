from odoo import models, fields

class DampakSarpras(models.Model):
    _name = "humanitarian.dampaksarpras"
    _description = 'Dampak Sarpras'

    dampak_site_id = fields.Many2one('humanitarian.sitrep', string='Situation')
    kerusakan = fields.Char(string="Kerusakan")
    jumlah = fields.Integer(string="Jumlah")
    satuan = fields.Char(string="Satuan")