from odoo import models, fields

class Province(models.Model):
    _name = "humanitarian.humanitarian_provinsi"
    _description = 'Provinsi'
    _rec_name = "provinsi"

    provinsi = fields.Char(string="Nama Provinsi", required=False)
    kdprov = fields.Char(string="Kode Provinsi", size=16, required=False)