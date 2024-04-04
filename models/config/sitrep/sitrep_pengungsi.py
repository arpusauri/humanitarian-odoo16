from odoo import models, fields

class Pengungsi(models.Model):
    _name = "humanitarian.sitrep_pengungsi"
    _description = 'Pengungsi'

    lokasi_pengungsian = fields.Char(string="Lokasi Pengungsian")
    jumlah = fields.Integer(string="Jumlah")
    pengungsi_site_id = fields.Many2one('humanitarian.humanitarian_sitrep', string='Situation')