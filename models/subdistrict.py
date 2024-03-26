from odoo import api, models, fields

class Subdistrict(models.Model):
    _name = 'humanitarian.subdistrict'
    _description = 'Data Kelurahan'
    _rec_name = 'kel'

    kel = fields.Char(string="Nama Kelurahan", required=False) 
    kdkel = fields.Char(string="Nomor Induk Desa", size=16, required=False) 
    kdkec = fields.Char(string="Kode Kecamatan", size=16, required=False)
    kec = fields.Many2one(comodel_name='humanitarian.district', string='Nama Kecamatan', required=False)
    kdkota = fields.Char(string="Kode Kota", size=16, required=False)
    kota = fields.Many2one(comodel_name='humanitarian.city', string='Nama Kota', required=False)
    provinsi = fields.Many2one(comodel_name='humanitarian.province', string='Nama Provinsi', required=False)
    kdprov = fields.Char(string="Kode Provinsi", size=16, required=False)
     
    @api.onchange('district')
    def _onchange_kdkec(self):
        self.kdkec = self.kec.kdkec
    
    @api.onchange('kota')
    def _onchange_kdkota(self):
        self.kdkota = self.kota.kdkota

    @api.onchange('provinsi')
    def _onchange_kdprov(self):
        self.kdprov = self.provinsi.kdprov