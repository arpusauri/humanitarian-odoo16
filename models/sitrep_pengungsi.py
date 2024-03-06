from odoo import models, fields

class Pengungsi(models.Model):
    _name = "humanitarian.pengungsi"
    _description = 'Pengungsi'

    lokasi_pengungsian = fields.Char(string="Lokasi Pengungsian")
    site_id = fields.Many2one('humanitarian.sitrep', string='Situation')
    jumlah = fields.Integer(string="Jumlah")