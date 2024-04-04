from odoo import api, models, fields

class SitrepDocumentation(models.Model):
    _name = "humanitarian.sitrep_dokumentasi"
    _description = 'Dokumentasi Situation Reports'

    image = fields.Binary(string='Image')
    dok_site_id = fields.Many2one('humanitarian.humanitarian_sitrep', string='Situation')
