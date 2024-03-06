from odoo import models, fields

class Distrep(models.Model):
    _name = "humanitarian.distrep"
    _description = 'Distrep'
    _rec_name = 'distrep_id'

    sitrep_id = fields.Many2one('humanitarian.sitrep', string="Nama Kejadian")
    distrep_id = fields.Many2one('humanitarian.jenis_kejadian', string="Jenis Kejadian")
    pic = fields.Many2one('humanitarian.pic', string="PIC")
    province_id = fields.Many2one('humanitarian.province', string="Provinsi")
    city_id = fields.Many2one('humanitarian.city', string="Kota/Kabupaten")
    district_id = fields.Many2one('humanitarian.district', string="Kecamatan")
    subdistrict_id = fields.Many2one('humanitarian.subdistrict', string="Desa")
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