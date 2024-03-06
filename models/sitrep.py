from odoo import models, fields

class Sitrep(models.Model):
    _name = "humanitarian.sitrep"
    _description = 'Sitrep'

    jenis_kejadian = fields.Many2one('humanitarian.jenis_kejadian', string='Jenis Kejadian')
    nama_kejadian = fields.Char(string="Nama Kejadian")
    pic = fields.Many2one('humanitarian.pic', string='PIC Lapangan')
    province_id = fields.Many2one('humanitarian.Provinsi', string='Provinsi')
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