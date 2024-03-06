from odoo import models, fields

class District(models.Model):
    _name = "humanitarian.district"
    _description = 'District'
    _rec_name = "district_id"

    district_id = fields.Char(string="District")