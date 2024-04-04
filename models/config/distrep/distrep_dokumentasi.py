from odoo import api, models, fields

class DistrepDocumentation(models.Model):
    _name = "humanitarian.distrep_dokumentasi"
    _description = 'Dokumentasi Distribution Reports'

    image = fields.Binary(string="Image")
    dok_dist_id = fields.Many2one('humanitarian.humanitarian_distrep', string='Distribution')