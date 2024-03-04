from odoo import models, fields

class SitrepDocumentation(models.Model):
    _name = "humanitarian.sitrep_documentation"
    _description = 'Sitrep Documentation'

    image = fields.Binary(string="Image")
    site_id = fields.Char(string="Situation")