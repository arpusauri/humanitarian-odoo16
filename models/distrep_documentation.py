from odoo import models, fields

class DistrepDocumentation(models.Model):
    _name = "humanitarian.distrep_documentation"
    _description = 'Distrep Documentation'

    image = fields.Binary(string="Image")
    distrep_id = fields.Many2one('humanitarian.distrep', string='Distribution')
