from odoo import models, fields

class Subdistrict(models.Model):
    _name = "humanitarian.subdistrict"
    _description = 'Subdistrict'

    subdistrict_id = fields.Char(string="Subdistrict")