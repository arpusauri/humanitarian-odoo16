from odoo import models, fields

class Mitra(models.Model):
    _name = "humanitarian.distrep_mitra"
    _description = 'Mitra'

    mitra = fields.Char(string="Mitra")
    mitra_dist_id = fields.Many2one('humanitarian.humanitarian_distrep', string='Distribution')