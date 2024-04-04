from odoo import models, fields

class Sitrep(models.Model):
    _name = 'humanitarian.humanitarian_sitrep'
    _description = 'Situation Reports'
    _rec_name = 'nama_kejadian'

    jenis_kejadian = fields.Many2one('humanitarian.humanitarian_jenis_kejadian', string='Jenis Kejadian')
    nama_kejadian = fields.Char(string='Nama Kejadian')
    jumlah = fields.Many2one('humanitarian.sitrep_lokasiterdampak', string='Jumlah')
    
    provinsi_id =  fields.Many2one(comodel_name='humanitarian.humanitarian_provinsi', string = 'Provinsi')
    kota_id =  fields.Many2one(comodel_name='humanitarian.humanitarian_kota', string = 'Kota')
    kec_id = fields.Many2one(comodel_name='humanitarian.humanitarian_kec', string = 'Kecamatan')
    kel_id =  fields.Many2one(comodel_name='humanitarian.humanitarian_kel', string = 'Kelurahan')

    alamat_lengkap = fields.Text(string='Alamat Lengkap')
    latitude = fields.Text(string='Latitude')
    longitude = fields.Text(string='Longitude')
    state = fields.Selection([
        ('draft', 'Draft'),
        ('publish', 'Publish')
    ], string='State')
    pic = fields.Many2one(comodel_name='humanitarian.humanitarian_pic', inverse_name='pic_id', string='PIC')
    
    dampak_site_id = fields.One2many(comodel_name='humanitarian.sitrep_dampaksarpras', inverse_name='dampak_site_id', string='Dampak SarPras')
    lokasi_site_id = fields.One2many(comodel_name='humanitarian.sitrep_lokasi_terdampak', inverse_name='lokasi_site_id', string='Lokasi Terdampak')
    korban_site_id = fields.One2many(comodel_name='humanitarian.sitrep_jmlkorban', inverse_name='korban_site_id', string='Jumlah Korban')
    pengungsi_site_id = fields.One2many(comodel_name='humanitarian.sitrep_pengungsi', inverse_name='pengungsi_site_id', string='Pengungsi')
    kebutuhan_site_id = fields.One2many(comodel_name='humanitarian.sitrep_kebutuhan_mendesak', inverse_name='kebutuhan_site_id', string='Kebutuhan Mendesak')
    dok_site_id = fields.One2many(comodel_name='humanitarian.sitrep_dokumentasi', inverse_name='dok_site_id', string='Dokumentasi Site Report')