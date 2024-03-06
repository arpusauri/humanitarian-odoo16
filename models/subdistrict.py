from odoo import models, fields

class Subdistrict(models.Model):
    _name = "humanitarian.subdistrict"
    _description = 'Subdistrict'
    _rec_name = "subdistrict_id"

    subdistrict_id = fields.Char(string="Subdistrict")