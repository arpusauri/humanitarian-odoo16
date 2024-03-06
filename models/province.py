from odoo import models, fields

class Province(models.Model):
    _name = "humanitarian.province"
    _description = 'Provinsi'
    _rec_name = "province_id"

    province_id = fields.Char(string="Provinsi")
    