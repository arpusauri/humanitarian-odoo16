from odoo import models, fields

class LokasiTerdampak(models.Model):
    _name = "humanitarian.lokasi_terdampak"
    _description = 'Lokasi Terdampak'

    district_id = fields.Many2one('humanitarian.district', string='District')
    lokasi_site_id = fields.Many2one('humanitarian.sitrep', string='Situation')
    jumlah = fields.Integer(string="Jumlah")
    
    