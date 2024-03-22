from odoo import models, fields

class SitrepDocumentation(models.Model):
    _name = "humanitarian.sitrep_documentation"
    _description = 'Sitrep Documentation'

    image = fields.Binary(string="Image")
    doc_site_id = fields.Many2one('humanitarian.sitrep', string='Situation')