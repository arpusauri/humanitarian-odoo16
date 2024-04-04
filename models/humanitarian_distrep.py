from odoo import models, fields

class Distrep(models.Model):
    _name = "humanitarian.humanitarian_distrep"
    _description = 'Distribution Reports'
    _rec_name = 'distrep_id'

    sitrep_id = fields.Many2one('humanitarian.humanitarian_sitrep', string="Nama Kejadian")
    distrep_id = fields.Many2one('humanitarian.humanitarian_jenis_kejadian', string="Jenis Kejadian")
    pic = fields.Many2one('humanitarian.humanitarian_pic', string="PIC")

    provinsi_id =  fields.Many2one(comodel_name='humanitarian.humanitarian_provinsi', string = 'Provinsi')
    kota_id =  fields.Many2one(comodel_name='humanitarian.humanitarian_kota', string = 'Kota')
    kec_id = fields.Many2one(comodel_name='humanitarian.humanitarian_kec', string = 'Kecamatan')
    kel_id =  fields.Many2one(comodel_name='humanitarian.humanitarian_kel', string = 'Kelurahan')

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

    cluster_dist_id = fields.One2many(comodel_name='humanitarian.distrep_cluster', inverse_name='cluster_dist_id', string='Cluster')
    mitra_dist_id = fields.One2many(comodel_name='humanitarian.distrep_mitra', inverse_name='mitra_dist_id', string='Mitra')
    dok_dist_id = fields.One2many(comodel_name='humanitarian.distrep_dokumentasi', inverse_name='dok_dist_id', string='Dokumentasi Distribution Report')
