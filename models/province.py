from odoo import models, fields

class Province(models.Model):
    _name = "humanitarian.province"
    _description = 'Provinsi'

    province_id = fields.Char(string="Provinsi")