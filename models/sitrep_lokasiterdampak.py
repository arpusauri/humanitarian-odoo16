from odoo import models, fields

class LokasiTerdampak(models.Model):
    _name = "humanitarian.lokasi_terdampak"
    _description = 'Lokasi Terdampak'

    district_id = fields.Char(string="Kecamatan")
    site_id = fields.Char(string="Situation")
    jumlah = fields.Integer(string="Jumlah")