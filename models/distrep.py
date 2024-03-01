from odoo import models, fields

class Distrep(models.Model):
    _name = "humanitarian.distrep"
    _description = 'Distrep'


    siterep_id = fields.Char(string="Nama Kejadian")
    pic = fields.Char(string="PIC")
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
    no_spk = fields.Char(string="No. SPK")
    tanggal_penyaluran = fields.Date(string="Tanggal Penyaluran")
    jml_pm = fields.Integer(string="Jumlah PM")
    jml_relawan = fields.Integer(string="Jumlah Relawan")