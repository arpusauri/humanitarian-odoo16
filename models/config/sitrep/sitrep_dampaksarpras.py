from odoo import models, fields

class DampakSarpras(models.Model):
    _name = "humanitarian.sitrep_dampaksarpras"
    _description = 'Dampak Sarana & Prasarana'

    dampak_site_id = fields.Many2one('humanitarian.humanitarian_sitrep', string='Situation')
    kerusakan = fields.Char(string="Kerusakan")
    jumlah = fields.Integer(string="Jumlah")
    satuan = fields.Char(string="Satuan")