from odoo import models, fields

class LokasiTerdampak(models.Model):
    _name = "humanitarian.sitrep_lokasi_terdampak"
    _description = 'Lokasi Terdampak'

    kec_id = fields.Many2one('humanitarian.humanitarian_kec', string='Kecamatan')
    lokasi_site_id = fields.Many2one('humanitarian.humanitarian_sitrep', string='Situation ID')
    jumlah = fields.Integer(string="Jumlah")
    
    