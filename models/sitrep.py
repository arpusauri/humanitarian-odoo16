from odoo import models, fields

class Sitrep(models.Model):
    _name = "humanitarian.sitrep"
    _description = 'Sitrep'


    jenis_kejadian = fields.Char(string="Jenis Kejadian")
    nama_kejadian = fields.Char(string="Nama Kejadian")
    province_id = fields.Char(string="Provinsi")
    city_id = fields.Char(string="Kota/Kabupaten")
    district_id = fields.Char(string="Kecamatan")
    subdistrict_id = fields.Char(string="Desa")
    alamat_lengkap = fields.Text(string="Alamat Lengkap")
    latitude = fields.Text(string="Latitude")
    longitude = fields.Text(string="Longitude")
    state = fields.Selection([
        ('draft', 'Draft'),
        ('publish', 'Publish')
    ], string='State')