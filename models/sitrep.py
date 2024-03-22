from odoo import models, fields

class Sitrep(models.Model):
    _name = "humanitarian.sitrep"
    _description = 'Sitrep'
    _rec_name = 'nama_kejadian'

    jenis_kejadian = fields.Many2one('humanitarian.jenis_kejadian', string='Jenis Kejadian')
    nama_kejadian = fields.Char(string="Nama Kejadian")
    jumlah = fields.Many2one('humanitarian.sitrep_lokasiterdampak', string='Jumlah')
    province_id = fields.Many2one('humanitarian.province', string='Provinsi')
    city_id = fields.Many2one('humanitarian.city', domain="[('province', '=', province_id)]", string="Kota/Kabupaten")
    district_id = fields.Many2one('humanitarian.district', domain="[('city', '=', city_id)]", string="Kecamatan")
    subdistrict_id = fields.Many2one('humanitarian.subdistrict', string="Desa")
    alamat_lengkap = fields.Text(string="Alamat Lengkap")
    latitude = fields.Text(string="Latitude")
    longitude = fields.Text(string="Longitude")
    state = fields.Selection([
        ('draft', 'Draft'),
        ('publish', 'Publish')
    ], string='State')
    pic_id = fields.One2many(comodel_name="humanitarian.pic", inverse_name="pic", string="PIC")
    dampak_site_id = fields.One2many(comodel_name="humanitarian.dampaksarpras", inverse_name="dampak_site_id", string="Dampak SarPras")
    lokasi_site_id = fields.One2many(comodel_name="humanitarian.lokasi_terdampak", inverse_name="lokasi_site_id", string="Lokasi Terdampak")
    korban_site_id = fields.One2many(comodel_name="humanitarian.jml_korbanjiwa", inverse_name="korban_site_id", string="Jumlah Korban")
    kebutuhan_site_id = fields.One2many(comodel_name="humanitarian.kebutuhan_mendesak", inverse_name="kebutuhan_site_id", string="Kebutuhan Mendesak")
    doc_site_id = fields.One2many(comodel_name="humanitarian.sitrep_documentation", inverse_name="doc_site_id", string="Dokumentasi Site Report")