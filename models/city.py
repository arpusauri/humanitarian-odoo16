from odoo import models, fields

class City(models.Model):
    _name = "humanitarian.city"
    _description = 'City'

    name = fields.Char(string="City")
    sitrep_id = fields.Many2one('humanitarian.sitrep', string="Sitrep ID")