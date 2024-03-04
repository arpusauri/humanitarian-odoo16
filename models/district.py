from odoo import models, fields

class District(models.Model):
    _name = "humanitarian.district"
    _description = 'District'

    district_id = fields.Char(string="District")